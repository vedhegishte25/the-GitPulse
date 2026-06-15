from fastapi import APIRouter, HTTPException
from backend.services import github_client

router = APIRouter(
    prefix="/contributors",
    tags=["Contributors"],
)


@router.get("/{owner}/{repo}")
async def get_contributors(owner: str, repo: str):
    """Get contributors list with contribution counts."""
    try:
        data = await github_client.get_contributors(owner, repo)
        total_contributions = sum(c["contributions"] for c in data)
        return {
            "total_contributors": len(data),
            "total_contributions": total_contributions,
            "contributors": [
                {
                    "rank": index + 1,
                    "username": c["login"],
                    "avatar": c["avatar_url"],
                    "contributions": c["contributions"],
                    "profile": c["html_url"],
                    "percentage": round(
                        (c["contributions"] / total_contributions) * 100, 2
                    ),
                }
                for index, c in enumerate(data)
            ],
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{owner}/{repo}/leaderboard")
async def get_leaderboard(owner: str, repo: str):
    """Get top 10 contributors leaderboard."""
    try:
        data = await github_client.get_contributors(owner, repo)
        top10 = data[:10]
        total_contributions = sum(c["contributions"] for c in data)
        return {
            "leaderboard": [
                {
                    "rank": index + 1,
                    "username": c["login"],
                    "avatar": c["avatar_url"],
                    "contributions": c["contributions"],
                    "profile": c["html_url"],
                    "percentage": round(
                        (c["contributions"] / total_contributions) * 100, 2
                    ),
                }
                for index, c in enumerate(top10)
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{owner}/{repo}/bus-factor")
async def get_bus_factor(owner: str, repo: str):
    """
    Calculate bus factor — how many contributors own 50% of all commits.
    Low number = high risk (project depends on very few people).
    """
    try:
        data = await github_client.get_contributors(owner, repo)
        total = sum(c["contributions"] for c in data)
        cumulative = 0
        bus_factor = 0
        for c in data:
            cumulative += c["contributions"]
            bus_factor += 1
            if cumulative >= total * 0.5:
                break
        risk = "High Risk 🔴" if bus_factor <= 2 else "Medium Risk 🟡" if bus_factor <= 5 else "Healthy 🟢"
        return {
            "bus_factor": bus_factor,
            "risk_level": risk,
            "explanation": f"{bus_factor} contributor(s) own 50% of all commits",
            "total_contributors": len(data),
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{owner}/{repo}/new-contributors")
async def get_new_contributors(owner: str, repo: str):
    """Get contributors with less than 10 contributions (new/first-time)."""
    try:
        data = await github_client.get_contributors(owner, repo)
        new_contributors = [c for c in data if c["contributions"] <= 10]
        return {
            "total_new_contributors": len(new_contributors),
            "new_contributors": [
                {
                    "username": c["login"],
                    "avatar": c["avatar_url"],
                    "contributions": c["contributions"],
                    "profile": c["html_url"],
                }
                for c in new_contributors
            ],
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))