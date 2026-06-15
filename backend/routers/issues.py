from fastapi import APIRouter, HTTPException
from backend.services import github_client
from datetime import datetime

router = APIRouter(
    prefix="/issues",
    tags=["Issues & PRs"],
)


@router.get("/{owner}/{repo}")
async def get_issues(owner: str, repo: str, state: str = "all"):
    """Get issues summary for a repository."""
    try:
        data = await github_client.get_issues(owner, repo, state)

        # Filter out pull requests (GitHub returns PRs in issues endpoint)
        issues_only = [i for i in data if "pull_request" not in i]

        open_issues = [i for i in issues_only if i["state"] == "open"]
        closed_issues = [i for i in issues_only if i["state"] == "closed"]

        return {
            "total": len(issues_only),
            "open": len(open_issues),
            "closed": len(closed_issues),
            "close_rate": round(
                (len(closed_issues) / len(issues_only)) * 100, 2
            ) if issues_only else 0,
            "issues": [
                {
                    "id": i["number"],
                    "title": i["title"],
                    "state": i["state"],
                    "author": i["user"]["login"],
                    "created_at": i["created_at"],
                    "closed_at": i["closed_at"],
                    "labels": [l["name"] for l in i["labels"]],
                    "comments": i["comments"],
                    "url": i["html_url"],
                }
                for i in issues_only
            ],
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{owner}/{repo}/pulls")
async def get_pull_requests(owner: str, repo: str, state: str = "all"):
    """Get pull requests summary for a repository."""
    try:
        data = await github_client.get_pulls(owner, repo, state)

        open_prs = [pr for pr in data if pr["state"] == "open"]
        closed_prs = [pr for pr in data if pr["state"] == "closed"]
        merged_prs = [pr for pr in data if pr.get("merged_at")]

        return {
            "total": len(data),
            "open": len(open_prs),
            "closed": len(closed_prs),
            "merged": len(merged_prs),
            "merge_rate": round(
                (len(merged_prs) / len(data)) * 100, 2
            ) if data else 0,
            "pull_requests": [
                {
                    "id": pr["number"],
                    "title": pr["title"],
                    "state": pr["state"],
                    "author": pr["user"]["login"],
                    "created_at": pr["created_at"],
                    "merged_at": pr.get("merged_at"),
                    "labels": [l["name"] for l in pr["labels"]],
                    "url": pr["html_url"],
                }
                for pr in data
            ],
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{owner}/{repo}/labels")
async def get_label_analysis(owner: str, repo: str):
    """Get label distribution across issues."""
    try:
        data = await github_client.get_issues(owner, repo, "all")
        issues_only = [i for i in data if "pull_request" not in i]

        label_counts = {}
        for issue in issues_only:
            for label in issue["labels"]:
                name = label["name"]
                label_counts[name] = label_counts.get(name, 0) + 1

        sorted_labels = sorted(
            label_counts.items(), key=lambda x: x[1], reverse=True
        )

        return {
            "total_labels": len(sorted_labels),
            "labels": [
                {"label": label, "count": count}
                for label, count in sorted_labels
            ],
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{owner}/{repo}/stale")
async def get_stale_issues(owner: str, repo: str, days: int = 30):
    """Get issues that have been open for more than X days."""
    try:
        data = await github_client.get_issues(owner, repo, "open")
        issues_only = [i for i in data if "pull_request" not in i]

        now = datetime.utcnow()
        stale = []
        for issue in issues_only:
            created = datetime.strptime(
                issue["created_at"], "%Y-%m-%dT%H:%M:%SZ"
            )
            age_days = (now - created).days
            if age_days >= days:
                stale.append({
                    "id": issue["number"],
                    "title": issue["title"],
                    "author": issue["user"]["login"],
                    "created_at": issue["created_at"],
                    "age_days": age_days,
                    "url": issue["html_url"],
                })

        stale.sort(key=lambda x: x["age_days"], reverse=True)

        return {
            "stale_threshold_days": days,
            "total_stale": len(stale),
            "stale_issues": stale,
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))