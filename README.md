### Task 1. Creating the Project Structure

- Each layer should be a separate module.
- The project structure must include the following layers: **web**, **domain**, **datasource**, and **di**.
- The **web** layer must contain the following packages for client interaction: model, module, route, and mapper.
- The **domain** layer must include the model and service packages to implement business logic.
- The **datasource** layer must include the model, repository, and mapper packages for data handling (e.g., database operations).
- The **di** layer contains configurations for dependency injection.

### Task 2. Implementing the Domain Layer

- Define the game board model as an integer matrix.
- Define the current game model, which includes a UUID and the game board.
- Define a service interface with the following methods:
  - A method to determine the next move in the current game using the Minimax algorithm.
  - A method to validate the current game board (checking that previous moves have not been altered).
  - A method to check if the game has ended.
- Place models, interfaces, and implementations in separate files.

### Task 3. Implementing the Datasource Layer

- Implement a storage class for current games.
- Use thread-safe collections for storage.
- Define models for the game board and the current game.
- Implement mappers between the domain and data source models (domain<->datasource).
- Implement a repository to work with the storage class that includes the following methods:
  - A method to save the current game.
  - A method to retrieve the current game.
- Create a class that implements the service interface and accepts the repository as a parameter to work with the storage class.
- Place models, interfaces, and implementations in separate files.

### Task 4. Implementing the Web Layer

- Define models for the game board and the current game.
- Implement mappers between the domain and web models (domain<->web).
- Implement a Flask controller with a POST method, /game/{current_game_UUID}, that accepts a current game with a user-updated game board and returns a current game with a computer-updated game board.
- If an invalid game with an updated board is sent, return an error with a description.
- Support multiple games running simultaneously.
- Models, interfaces, and implementations should be in separate files.

### Task 5. Implementing the DI Layer

- Implement a Container class that defines the dependency graph.
- It must include at least:
  - A singleton storage class.
  - A repository for working with the storage class.
  - A service for working with the repository.