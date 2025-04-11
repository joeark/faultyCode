#include <iostream>
#include <thread>
#include <vector>
#include <mutex>
#include <chrono>
#include <random>

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
    std::vector<Task*> tasks;
    std::mutex mtx;

public:
    void addTask(Task* task) {
        // Missing lock leads to potential race condition
        tasks.push_back(task);
    }

    void runTasks() {
        std::vector<std::thread> threads;

        for (auto task : tasks) {
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
        for (auto task : tasks) {
            std::cout << "Task [" << task->name << "] status: "
                      << (task->isCompleted ? "Done" : "Pending") << std::endl;
        }
    }

    ~TaskManager() {
        // Intentional memory leak: not deleting dynamically allocated tasks
    }
};

int main() {
    srand(static_cast<unsigned>(time(0)));

    TaskManager manager;

    // Uninitialized pointer - leads to undefined behavior
    Task* uninitializedTask;
    manager.addTask(uninitializedTask);

    for (int i = 0; i < 5; ++i) {
        Task* t = new Task(i, "Task_" + std::to_string(i));
        manager.addTask(t);
    }

    manager.runTasks();
    manager.printStatus();

    return 0;
}
