function addTask() {
  let task = document.getElementById("task-item");
  console.log(task.value);
  let list = document.getElementById("task-list")
  list.innerHTML += `<li onclick="removeTask(this)">${task.value}</li>`
}

function removeTask(task) {
  task.remove()
}

const taskInput = document.getElementById("task-item");

taskInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        addTask();
    }
});