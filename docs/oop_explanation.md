This project uses object oriented programming in the following ways:

- **Encapsulation:** Each model handler stores its own state (e.g., `loaded` flag, `model` object) and exposes `load()` / `run()` methods.
- **Polymorphism:** Both `TextModelHandler` and `ImageModelHandler` implement the same interface (`load()` and `run()`), so the GUI can call `.run()` without needing model-specific logic.
- **Inheritance / Mixins:** `ModelHandler` is the base class. Handlers also inherit a small `Logger` mixin to demonstrate multiple inheritance.
- **Decorator / Timing:** A simple `simple_timer` decorator prints how long `load()` and `run()` took, showing layered behaviour without changing method bodies.