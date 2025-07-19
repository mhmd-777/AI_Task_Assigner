// 📁 scripts/employees.js

window.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("employeeForm");
  const list = document.getElementById("employeeList");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const name = document.getElementById("empName").value;
    const skills = document.getElementById("empSkills").value;
    const availability = document.getElementById("empAvailability").value;
    const experience = parseInt(document.getElementById("empExperience").value);

    await fetch("/employees/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, skills, availability, experience })
    });

    form.reset();
    loadEmployees();
  });

  async function loadEmployees() {
    const res = await fetch("/employees/");
    const employees = await res.json();
    list.innerHTML = "";

    employees.forEach(emp => {
      const li = document.createElement("li");
      li.className = "employee-item";
      li.innerHTML = `
        <div class="emp-main">
          <strong>${emp.name}</strong>
          <span class="emp-sub">${emp.skills}</span>
          <span class="emp-sub">${emp.availability}, ${emp.experience} yrs</span>
        </div>
        <div class="emp-task">
          <span class="badge">${emp.assigned_task || "Unassigned"}</span>
          ${emp.assigned_task !== "None" && emp.assigned_task !== null ? `<button class="btn-clear" data-id="${emp.id}">🧹</button>` : ""}
          <button class="btn-delete" data-id="${emp.id}">🗑</button>
        </div>
      `;
      list.appendChild(li);
    });

    // Delete logic
    list.querySelectorAll(".btn-delete").forEach(btn => {
      btn.addEventListener("click", async () => {
        const id = btn.getAttribute("data-id");
        await fetch(`/employees/${id}`, { method: "DELETE" });
        loadEmployees();
      });
    });

    // Clear task logic
    list.querySelectorAll(".btn-clear").forEach(btn => {
      btn.addEventListener("click", async () => {
        const id = btn.getAttribute("data-id");
        await fetch(`/employees/${id}/clear-task`, { method: "POST" });
        loadEmployees();
      });
    });
  }

  loadEmployees();
});
