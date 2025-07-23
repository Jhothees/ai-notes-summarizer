function downloadSummary() {
    const summary = document.getElementById("summaryBox").value;
    const blob = new Blob([summary], { type: "text/plain" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "summary.txt";
    link.click();
}
const toggle = document.getElementById("theme-toggle");

if (localStorage.getItem("darkMode") === "enabled") {
    document.body.classList.add("dark");
    toggle.checked = true;
}

toggle.addEventListener("change", () => {
    document.body.classList.toggle("dark");
    if (document.body.classList.contains("dark")) {
        localStorage.setItem("darkMode", "enabled");
    } else {
        localStorage.setItem("darkMode", "disabled");
    }
});
