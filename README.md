# NandemoTask-App

## Git branch 전략

- **main** - **develop** - **feature/~~** 세 branch로 운영.
```mermaid
sequenceDiagram
Note left of main: initial version
main-->> develop: checkout
develop-->>feature/work1: checkout
develop-->>feature/work2: checkout
feature/work1->>develop: merge
develop-->>feature/work3: checkout
Note left of main: version 1.0
develop->>main: merge
```

## Code Style

### 1. naming rule
- 변수(variable) : **카멜 케이스** ex) curName, myName

- 클래스(class) : **파스칼 케이스** ex) Student, BandingMachine

- 함수(function) :  **스네이크 케이스** ex) get_host, make_user

## Library
## Environment
