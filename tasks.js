document.addEventListener('DOMContentLoaded', () => {
  loadTasks();
  document.getElementById('taskForm').addEventListener('submit', addTask);
});

async function loadTasks() {
  const res = await fetch('/tasks');
  const tasks = await res.json();
  const list = document.getElementById('taskList');
  list.innerHTML = '';

  tasks.forEach(task => {
    const div = document.createElement('div');
    div.className = 'task-item';

    const info = document.createElement('div');
    info.className = 'info';
    info.innerHTML = `<strong>${task.title}</strong><br>Status: ${task.completed ? '✅ Completed' : (task.assigned_to ? `Assigned to ID ${task.assigned_to}` : 'Unassigned')}`;

    const actions = document.createElement('div');
    actions.className = 'actions';

    if (!task.assigned_to && !task.completed) {
      actions.innerHTML += `
        <select id="mode-${task.id}">
          <option value="ai">AI Agent</option>
          <option value="rule">Rule-Based</option>
        </select>
        <button class="btn-assign" data-id="${task.id}">Assign</button>
      `;
    }

    if (!task.completed) {
      actions.innerHTML += `<button class="btn-complete" onclick="markComplete(${task.id})">✅</button>`;
    }

    actions.innerHTML += `<button class="btn-delete" onclick="deleteTask(${task.id})">🗑</button>`;

    div.appendChild(info);
    div.appendChild(actions);
    list.appendChild(div);
  });

  document.querySelectorAll(".btn-assign").forEach(btn => {
    btn.addEventListener("click", async () => {
      const id = btn.getAttribute("data-id");
      const mode = document.getElementById(`mode-${id}`).value;

      const res = await fetch(`/tasks/${id}`);
      const task = await res.json();

      const endpoint = mode === "ai" ? "/assign-task/ai" : "/assign-task/rule";

      await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: task.title })
      });

      loadTasks();
    });
  });
}

async function addTask(e) {
  e.preventDefault();
  const title = document.getElementById('taskInput').value.trim();
  if (!title) return;

  await fetch('/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title })
  });

  document.getElementById('taskInput').value = '';
  loadTasks();
}

async function deleteTask(id) {
  await fetch(`/tasks/${id}`, { method: 'DELETE' });
  loadTasks();
}

async function markComplete(id) {
  await fetch(`/tasks/${id}/complete`, { method: 'POST' });
  loadTasks();
}
