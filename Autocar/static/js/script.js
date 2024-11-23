const cars = [];
const servers = [];
let tasks = [];

// Add cars dynamically
function initCars(num) {
    const road = document.getElementById("road");
    for (let i = 0; i < num; i++) {
        const car = document.createElement("img");
        car.src = "/static/images/car.jpg";
        car.classList.add("car");
        car.style.left = `${i * 120}px`;
        cars.push(car);
        road.appendChild(car);
    }
}

// Add servers dynamically
function initServers(num) {
    const serverContainer = document.getElementById("servers");
    for (let i = 0; i < num; i++) {
        const serverDiv = document.createElement("div");
        serverDiv.classList.add("server");
        serverDiv.innerHTML = `
            <img src="/static/images/server.png" alt="Server">
            <div>Server ${i + 1}</div>
            <div class="progress-bar"><div class="progress-bar-inner" id="ram-${i}" style="width: 100%;"></div></div>
            <div class="progress-bar"><div class="progress-bar-inner" id="storage-${i}" style="width: 100%;"></div></div>
        `;
        servers.push(serverDiv);
        serverContainer.appendChild(serverDiv);
    }
}

// Simulate task generation and processing
function startSimulation() {
    tasks = []; // Reset tasks
    cars.forEach((car, index) => {
        setTimeout(() => {
            const taskCount = Math.floor(Math.random() * 5) + 1;
            for (let i = 0; i < taskCount; i++) {
                const task = {
                    id: Math.random().toString(36).substr(2, 5),
                    car: index + 1,
                    ram: Math.floor(Math.random() * 200) + 50,
                    storage: Math.floor(Math.random() * 500) + 100,
                };
                tasks.push(task);
                offloadTask(task);
            }
        }, index * 2000);
    });
}

// Offload tasks to servers
function offloadTask(task) {
    const server = servers[Math.floor(Math.random() * servers.length)];
    const ramBar = server.querySelector(`#ram-${servers.indexOf(server)}`);
    const storageBar = server.querySelector(`#storage-${servers.indexOf(server)}`);

    // Simulate resource usage
    const ramUsage = parseInt(ramBar.style.width) - (task.ram / 1024) * 100;
    const storageUsage = parseInt(storageBar.style.width) - (task.storage / 4096) * 100;

    // Update progress bars
    if (ramUsage >= 0 && storageUsage >= 0) {
        ramBar.style.width = `${ramUsage}%`;
        storageBar.style.width = `${storageUsage}%`;
    } else {
        console.log(`Server overloaded: Task ${task.id} failed`);
    }
}

// Initialize
window.onload = () => {
    initCars(5);
    initServers(5);
};