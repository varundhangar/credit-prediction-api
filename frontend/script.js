const form = document.getElementById("predictionForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async function (event) {

    // Page reload hone se rokta hai
    event.preventDefault();

    // Form se values lena
    const data = {
        LIMIT_BAL: Number(document.getElementById("LIMIT_BAL").value),
        SEX: Number(document.getElementById("SEX").value),
        EDUCATION: Number(document.getElementById("EDUCATION").value),
        MARRIAGE: Number(document.getElementById("MARRIAGE").value),
        AGE: Number(document.getElementById("AGE").value),

        PAY_1: Number(document.getElementById("PAY_1").value),
        PAY_2: Number(document.getElementById("PAY_2").value),
        PAY_3: Number(document.getElementById("PAY_3").value),
        PAY_4: Number(document.getElementById("PAY_4").value),
        PAY_5: Number(document.getElementById("PAY_5").value),
        PAY_6: Number(document.getElementById("PAY_6").value),

        BILL_AMT1: Number(document.getElementById("BILL_AMT1").value),
        BILL_AMT2: Number(document.getElementById("BILL_AMT2").value),
        BILL_AMT3: Number(document.getElementById("BILL_AMT3").value),
        BILL_AMT4: Number(document.getElementById("BILL_AMT4").value),
        BILL_AMT5: Number(document.getElementById("BILL_AMT5").value),
        BILL_AMT6: Number(document.getElementById("BILL_AMT6").value),

        PAY_AMT1: Number(document.getElementById("PAY_AMT1").value),
        PAY_AMT2: Number(document.getElementById("PAY_AMT2").value),
        PAY_AMT3: Number(document.getElementById("PAY_AMT3").value),
        PAY_AMT4: Number(document.getElementById("PAY_AMT4").value),
        PAY_AMT5: Number(document.getElementById("PAY_AMT5").value),
        PAY_AMT6: Number(document.getElementById("PAY_AMT6").value)
    };


    // User ko batana ki prediction ho rahi hai
    resultDiv.innerHTML = "Predicting...";


    try {

        // FastAPI ko request bhejna
        const response = await fetch(
            "https://credit-prediction-api-sksq.onrender.com/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(data)
            }
        );


        // API response ko JSON me convert karna
        const result = await response.json();


        // Result frontend par show karna
        if (result.prediction === 1) {

            resultDiv.innerHTML = `
                <h2>⚠️ High Risk</h2>
                <p>${result.result}</p>
                <p>Default Probability:
                ${(result.default_probability * 100).toFixed(2)}%</p>
            `;

        } else {

            resultDiv.innerHTML = `
                <h2>✅ Low Risk</h2>
                <p>${result.result}</p>
                <p>Default Probability:
                ${(result.default_probability * 100).toFixed(2)}%</p>
            `;
        }


    } catch (error) {

        resultDiv.innerHTML = `
            <p>❌ Error connecting to API</p>
            <p>${error.message}</p>
        `;
    }

});