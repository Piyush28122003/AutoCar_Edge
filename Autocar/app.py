from flask import Flask, render_template, jsonify
from edge_server import EdgeServer
from car_simulator import Car
import csv  # Import csv library

app = Flask(__name__)

# Initialize edge servers
servers = [EdgeServer(i, ram=1024, storage=4096) for i in range(1, 6)]

# Initialize cars
cars = [Car(i) for i in range(1, 6)]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/simulate")
def simulate():
    all_tasks = []
    server_usage = []  # Create an empty list for server usage data

    for car in cars:
        tasks = car.generate_tasks(random.randint(10, 20))
        all_tasks.extend(tasks)

    for task in tasks:
        assigned = False
        for server in servers:
            if server.add_task(task):
                assigned = True
                server_usage.append((server.server_id, car.car_id, task["id"]))  # Record server, car, and task ID
                break
        if not assigned:
            task["status"] = "Pending"

    for server in servers:
        server.process_tasks()

    # Write server usage data to CSV file
    with open("server_usage.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Server ID", "Car ID", "Task ID"])  # Write header row
        writer.writerows(server_usage)

    return jsonify({"tasks": all_tasks, "servers": [{
        "id": server.server_id,
        "available_ram": server.available_ram,
        "available_storage": server.available_storage,
        "processed_tasks": len(server.processed_tasks)
    } for server in servers]})

@app.route("/server_usage")
def server_usage():
    # ... (existing code)

    server_data = {
        "servers": [
            {
                "id": server.server_id,
                "available_ram": server.available_ram,
                "available_storage": server.available_storage,
                "processed_tasks": len(server.processed_tasks)
            } for server in servers
        ],
        "tasks": [
            # ... (extract task information)
        ]
    }

    return jsonify(server_data)

if __name__ == "__main__":
    app.run(debug=True)