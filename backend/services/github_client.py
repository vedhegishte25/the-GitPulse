import httpx
from backend.config import get_settings

settings = get_settings()

GITHUB_API_BASE = "https://api.github.com"

HEADERS = {
    "Authorization": f"Bearer {settings.github_token}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


async def get_repo(owner: str, repo: str) -> dict:
    """Fetch basic repository information."""
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(
            f"{GITHUB_API_BASE}/repos/{owner}/{repo}",
            headers=HEADERS,
        )
        response.raise_for_status()
        return response.json()


async def get_contributors(owner: str, repo: str) -> list:
    """Fetch list of contributors for a repository."""
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(
            f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contributors",
            headers=HEADERS,
            params={"per_page": 100},
        )
        response.raise_for_status()
        return response.json()


async def get_commit_activity(owner: str, repo: str) -> list:
    """Fetch weekly commit activity for the last year."""
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(
            f"{GITHUB_API_BASE}/repos/{owner}/{repo}/stats/commit_activity",
            headers=HEADERS,
        )
        response.raise_for_status()
        return response.json()


async def get_languages(owner: str, repo: str) -> dict:
    """Fetch programming languages used in a repository."""
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(
            f"{GITHUB_API_BASE}/repos/{owner}/{repo}/languages",
            headers=HEADERS,
        )
        response.raise_for_status()
        return response.json()


async def get_issues(owner: str, repo: str, state: str = "all") -> list:
    """Fetch issues for a repository."""
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(
            f"{GITHUB_API_BASE}/repos/{owner}/{repo}/issues",
            headers=HEADERS,
            params={"per_page": 100, "state": state},
        )
        response.raise_for_status()
        return response.json()


async def get_pulls(owner: str, repo: str, state: str = "all") -> list:
    """Fetch pull requests for a repository."""
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(
            f"{GITHUB_API_BASE}/repos/{owner}/{repo}/pulls",
            headers=HEADERS,
            params={"per_page": 100, "state": state},
        )
        response.raise_for_status()
        return response.json()


async def get_releases(owner: str, repo: str) -> list:
    """Fetch releases for a repository."""
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(
            f"{GITHUB_API_BASE}/repos/{owner}/{repo}/releases",
            headers=HEADERS,
            params={"per_page": 100},
        )
        response.raise_for_status()
        return response.json()


async def get_code_frequency(owner: str, repo: str) -> list:
    """Fetch weekly code frequency (additions and deletions)."""
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response = await client.get(
            f"{GITHUB_API_BASE}/repos/{owner}/{repo}/stats/code_frequency",
            headers=HEADERS,
        )
        response.raise_for_status()
        return response.json()