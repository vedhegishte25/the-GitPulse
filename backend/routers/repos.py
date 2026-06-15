from fastapi import APIRouter, HTTPException
from backend.services import github_client

router = APIRouter(
    prefix="/repos",
    tags=["Repositories"],
)


@router.get("/{owner}/{repo}")
async def get_repository(owner: str, repo: str):
    """Get basic information about a repository."""
    try:
        data = await github_client.get_repo(owner, repo)
        return {
            "name": data["name"],
            "full_name": data["full_name"],
            "description": data["description"],
            "stars": data["stargazers_count"],
            "forks": data["forks_count"],
            "watchers": data["watchers_count"],
            "open_issues": data["open_issues_count"],
            "language": data["language"],
            "created_at": data["created_at"],
            "updated_at": data["updated_at"],
            "homepage": data["homepage"],
            "private": data["private"],
            "default_branch": data["default_branch"],
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{owner}/{repo}/contributors")
async def get_contributors(owner: str, repo: str):
    """Get contributors of a repository."""
    try:
        data = await github_client.get_contributors(owner, repo)
        return [
            {
                "username": c["login"],
                "avatar": c["avatar_url"],
                "contributions": c["contributions"],
                "profile": c["html_url"],
            }
            for c in data
        ]
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{owner}/{repo}/commit-activity")
async def get_commit_activity(owner: str, repo: str):
    """Get weekly commit activity for the last year."""
    try:
        data = await github_client.get_commit_activity(owner, repo)
        return data
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{owner}/{repo}/languages")
async def get_languages(owner: str, repo: str):
    """Get programming languages used in a repository."""
    try:
        data = await github_client.get_languages(owner, repo)
        total = sum(data.values())
        return [
            {
                "language": lang,
                "bytes": bytes_count,
                "percentage": round((bytes_count / total) * 100, 2),
            }
            for lang, bytes_count in sorted(
                data.items(), key=lambda x: x[1], reverse=True
            )
        ]
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{owner}/{repo}/releases")
async def get_releases(owner: str, repo: str):
    """Get releases of a repository."""
    try:
        data = await github_client.get_releases(owner, repo)
        return [
            {
                "tag": r["tag_name"],
                "name": r["name"],
                "published_at": r["published_at"],
                "prerelease": r["prerelease"],
                "url": r["html_url"],
            }
            for r in data
        ]
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{owner}/{repo}/code-frequency")
async def get_code_frequency(owner: str, repo: str):
    """Get weekly code additions and deletions."""
    try:
        data = await github_client.get_code_frequency(owner, repo)
        return [
            {
                "week": item[0],
                "additions": item[1],
                "deletions": item[2],
            }
            for item in data
        ]
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))