#include <iostream>
#include <thread>
#include <vector>
#include <mutex>
#include <chrono>
#include <random>
#include <memory>

class Task {
public:
    int id;
    std::string name;
    bool isCompleted;

    Task(int _id, std::string _name) : id(_id), name(_name), isCompleted(false) {}

    void execute() {
        std::cout << "Executing Task: " << name << " [ID: " << id << "]\n";
        std::this_thread::sleep_for(std::chrono::milliseconds(100 + (rand() % 400)));
        isCompleted = true;
    }
};

class TaskManager {
private:
    std::vector<std::unique_ptr<Task>> tasks;
    std::mutex mtx;

public:
    void addTask(std::unique_ptr<Task> task) {
        std::lock_guard<std::mutex> lock(mtx);
        tasks.push_back(std::move(task));
    }

    void runTasks() {
        std::vector<std::thread> threads;

        for (auto& task : tasks) {
            threads.push_back(std::thread([=]() {
                task->execute();
                std::cout << "Completed Task: " << task->name << std::endl;
            }));
        }

        for (auto& t : threads) {
            if (t.joinable()) {
                t.join();
            }
        }
    }

    void printStatus() {
        for (auto& task : tasks) {
            std::cout << "Task [" << task->name << "] status: "
                      << (task->isCompleted ? "Done" : "Pending") << std::endl;
        }
    }

    ~TaskManager() = default;
};

int main() {
    srand(static_cast<unsigned>(time(0)));

    TaskManager manager;

    for (int i = 0; i < 5; ++i) {
        manager.addTask(std::make_unique<Task>(i, "Task_" + std::to_string(i)));
    }

    manager.runTasks();
    manager.printStatus();

    return 0;
}