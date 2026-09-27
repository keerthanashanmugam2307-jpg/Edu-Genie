const taskSelect = document.getElementById("task");
const inputText = document.getElementById("inputText");
const generateBtn = document.getElementById("generateBtn");
const statusBox = document.getElementById("status");
const resultContent = document.getElementById("resultContent");


// Connect each task to its FastAPI endpoint
const endpoints = {
    qa: "/qa",
    explain: "/explain",
    quiz: "/quiz",
    summarize: "/summarize",
    learn: "/learn/recommendations"
};


// Generate button
generateBtn.addEventListener("click", async () => {

    const task = taskSelect.value;
    const text = inputText.value.trim();

    // Check input
    if (!text) {
        statusBox.textContent = "Please enter some text first.";
        resultContent.textContent = "";
        return;
    }

    // Get the correct API endpoint
    const endpoint = endpoints[task];

    // Show loading status
    generateBtn.disabled = true;
    generateBtn.textContent = "Generating...";
    statusBox.textContent = "EduGenie is processing your request...";
    resultContent.textContent = "";

    try {

        // Send request to FastAPI backend
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text
            })
        });

        // Check if backend returned an error
        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        // Convert response to JSON
        const data = await response.json();

        // Display result
        displayResult(data.result, task);

        statusBox.textContent = "Completed successfully!";

    } catch (error) {

        console.error(error);

        statusBox.textContent = "Something went wrong.";
        resultContent.textContent =
            "Unable to get a response from the server. Please check that the FastAPI server is running.";

    } finally {

        generateBtn.disabled = false;
        generateBtn.textContent = "Generate";
    }
});


// Display the result
function displayResult(result, task) {

    resultContent.innerHTML = "";

    // Quiz result
    if (task === "quiz" && Array.isArray(result)) {

        result.forEach((question, index) => {

            const questionDiv = document.createElement("div");
            questionDiv.className = "quiz-question";

            const questionTitle = document.createElement("h4");
            questionTitle.textContent =
                `${index + 1}. ${question.question}`;

            questionDiv.appendChild(questionTitle);

            question.options.forEach((option) => {

                const optionDiv = document.createElement("div");
                optionDiv.className = "quiz-option";
                optionDiv.textContent = option;

                questionDiv.appendChild(optionDiv);
            });

            const answer = document.createElement("p");
            answer.innerHTML =
                `<strong>Answer:</strong> ${question.answer}`;

            questionDiv.appendChild(answer);

            resultContent.appendChild(questionDiv);
        });

        return;
    }


    // Normal text result
    const resultParagraph = document.createElement("p");
    resultParagraph.textContent = result;

    resultContent.appendChild(resultParagraph);
}