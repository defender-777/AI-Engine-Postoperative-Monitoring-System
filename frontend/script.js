const BASE_URL = "http://127.0.0.1:8000";

// 1. Wound Prediction
async function predictWound() {
    let file = document.getElementById("woundImage").files[0];
    let form = new FormData();
    form.append("file", file);

    let res = await fetch(`${BASE_URL}/wound/predict`, {
        method: "POST",
        body: form
    });

    let data = await res.json();
    document.getElementById("result").innerHTML =
        `<h3>${data.wound_prediction.label} (${(data.wound_prediction.confidence * 100).toFixed(2)}%)</h3>`;
}

// 2. Vitals Check
async function checkVitals() {
    let hr = document.getElementById("hr").value;
    let temp = document.getElementById("temp").value;
    let spo2 = document.getElementById("spo2").value;

    let body = {
        hr: Number(hr),
        temp: Number(temp),
        spo2: Number(spo2)
    };

    let res = await fetch(`${BASE_URL}/vitals/check`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
    });

    let data = await res.json();
    document.getElementById("vitalResult").innerHTML =
        data.alerts.length ? data.alerts.join("<br>") : "✔ All vitals normal";
}

// 3. Full Risk Assessment
async function evaluateRisk() {
    let file = document.getElementById("riskImage").files[0];
    let hr = document.getElementById("riskHr").value;
    let temp = document.getElementById("riskTemp").value;
    let spo2 = document.getElementById("riskSpo2").value;

    let form = new FormData();
    form.append("file", file);
    form.append("hr", hr);
    form.append("temp", temp);
    form.append("spo2", spo2);

    let res = await fetch(`${BASE_URL}/risk/evaluate`, {
        method: "POST",
        body: form
    });

    let data = await res.json();
    document.getElementById("riskOutput").innerHTML =
        `<h3>Risk Score: ${data.risk_score.toFixed(2)}</h3>`;
}
