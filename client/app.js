
const API_URL = "http://127.0.0.1:5000/api/findings";

const findingsContainer = document.getElementById("findings");
const statusMessage = document.getElementById("status");

async function loadFindings() {
    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Unable to load audit findings.");
        }

        const findings = await response.json();

        findingsContainer.replaceChildren();

        findings.forEach((finding) => {
            const card = document.createElement("article");
            card.className = "finding-card";

            const title = document.createElement("h3");
            title.textContent = finding.title;

            const priority = document.createElement("span");
            priority.className = `priority ${finding.priority.toLowerCase()}`;
            priority.textContent = `${finding.priority} Priority`;

            const category = document.createElement("p");
            category.className = "category";
            category.textContent = finding.category;

            card.append(title, priority, category);
            findingsContainer.appendChild(card);
        });

        statusMessage.textContent =
            `${findings.length} audit findings loaded successfully.`;
    } catch (error) {
        statusMessage.textContent =
            "Could not load findings. Please check whether the backend is running.";
    }
}

loadFindings();
