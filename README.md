# GitPulse - keep a finger on the pulse of your codebase.
<img width="945" height="434" alt="Screenshot 2026-06-16 161826" src="https://github.com/user-attachments/assets/08363153-f26e-4053-8536-549f35d6d8c1" />
GitPulse is a GitHub analytics dashboard that gives you deep insights into any public GitHub repository in seconds. 
It pulls live data directly from the GitHub API and presents it in a clean, visual dashboard covering 
everything from commit activity and contributor performance to issues, pull requests and language breakdowns. 
The goal of GitPulse is to make repository intelligence accessible and beautiful, helping developers, teams and open source enthusiasts understand the health and momentum of any codebase at a glance. 
Whether you're evaluating a project to contribute to, monitoring your own repo, or comparing two libraries side by side
<br>
<img width="951" height="434" alt="Screenshot 2026-06-16 163417" src="https://github.com/user-attachments/assets/b573df46-a43d-485b-af6b-181ba8dffc66" />
<br>

---

## Features

- 📊 **Commit Activity** — Weekly commit heatmaps and code frequency charts showing additions vs deletions over the past year
- 👥 **Contributor Analytics** — Leaderboards, bus factor analysis, new contributor tracking and contribution percentages
- 🐛 **Issues & PRs** — Open vs closed trends, merge rates, label distribution and stale issue detection
- 🌐 **Language Breakdown** — Precise language percentages by bytes across the entire codebase
- ⚖️ **Repo Comparison** — Compare any two GitHub repositories side by side across all key metrics
- 🏥 **Health Score** — Bus factor risk, stale issues and PR merge rate combined into a single health signal

---

## Dashboard

The Dashboard is the heart of GitPulse. 
Once you search for any public GitHub repository, you land here with a complete analytics overview. 
It displays real-time repository metadata including stars, forks, watchers and open issues pulled directly from the GitHub API. 
The commit activity chart gives you a full year of weekly commit data at a glance, while the language breakdown donut chart shows exactly what percentage of the codebase is written in each language. 
The top contributors leaderboard highlights the most active developers, and the code frequency chart shows lines added 
versus deleted over time — a powerful signal for understanding whether a project is growing or being refactored.

<img width="945" height="434" alt="image" src="https://github.com/user-attachments/assets/7e0c38be-4731-45a1-be3b-96a1302503b7" />

---

## Contributors Page

The Contributors page goes deep into the people behind the code. 
Every contributor is displayed in a card grid with their avatar, username, total commits and percentage of the overall 
codebase they own. The top 10 leaderboard ranks contributors with gold, silver and bronze medals for the top three. 
A horizontal bar chart visualizes contribution distribution across the team. 
The Bus Factor section calculates how many contributors own 50% of all commits a low number is a risk signal, a high number means the project is healthy and distributed. 
New contributors with 10 or fewer commits are tracked separately to monitor community growth.

<img width="941" height="434" alt="image" src="https://github.com/user-attachments/assets/371dd2a3-9c03-4b73-961f-0c3db1336ecf" />

---

## Tech Stack

### Frontend
- HTML5, CSS3, Vanilla JavaScript
- Chart.js — for all data visualizations
- Dark / Light theme with CSS variables

### Backend
- Python 3.12
- FastAPI — REST API framework
- SQLAlchemy — async ORM
- Asyncpg — async PostgreSQL driver
- Httpx — async HTTP client for GitHub API calls

### Database
- PostgreSQL via Neon (serverless cloud PostgreSQL)
---

## API Used

- **GitHub REST API v3** — `https://api.github.com`
  - `/repos/{owner}/{repo}` — Repository metadata
  - `/repos/{owner}/{repo}/contributors` — Contributor list
  - `/repos/{owner}/{repo}/stats/commit_activity` — Weekly commit data
  - `/repos/{owner}/{repo}/languages` — Language breakdown
  - `/repos/{owner}/{repo}/issues` — Issues list
  - `/repos/{owner}/{repo}/pulls` — Pull requests
  - `/repos/{owner}/{repo}/releases` — Release history
  - `/repos/{owner}/{repo}/stats/code_frequency` — Code frequency

---

## Developer

**Ved Hegishte**
- GitHub: [@vedhegishte25](https://github.com/vedhegishte25)
- Email: vedhegishte11@gmail.com


---

## License

MIT License — feel free to use, modify and distribute this project with attribution.
