# Building and Deploying an API with FastAPI (python) and Azure


## Prerequisites

### Tools and Accounts Required:
1. **Python**: Ensure Python is installed on your system.
2. **Microsoft Azure Account**: If you are a student, you can get $100 free credits to try Azure.

---

## Project Setup

### Step 1: Set Up a Virtual Environment
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Run and Build the Web App
To launch the web application:
1. Run the following command:
   ```bash
   python -m run
   ```
2. The output should look similar to this:
   ```
   * Serving Flask app 'app'
   * Debug mode: on
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   * Running on http://127.0.0.1:5000
   ```
3. Open the URL [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to view the app.

---

## Building the API

The APIs are located in the `/api` folder. To create endpoints, open the `api/main_empty.py` file. A pre-filled version of the file can be found in `main.py`. Below is an explanation of the key endpoints:

### 1. Basic API Endpoint
#### Code:
```python
@app.get('/')
def read_root():
    return {"message": "Hello, World!"}
```
#### Explanation:
This is a simple endpoint that returns a greeting message. Accessible at `http://127.0.0.1:8000/`.

### 2. List Events
#### Code:
```python
@app.get('/api/v1/event_list')
def read_events():
    event_list = session.query(events.Event).all()
    return {"events": [event.to_dict() for event in event_list]}
```
#### Explanation:
Fetches a list of all events from the database. Accessible at `http://127.0.0.1:8000/api/v1/event_list`.

### 3. Get Participants by Event
#### Code:
```python
@app.get('/api/v1/participants/{event_id}')
def read_participants(event_id: int):
    participant_list = session.query(participants.Participant).filter_by(event_id=event_id).all()
    return {"participants": [participant.to_dict() for participant in participant_list]}
```
#### Explanation:
Retrieves participants for a specific event by event ID. Replace `{event_id}` in the URL with the actual ID.

### 4. Create Participant
#### Code:
```python
@app.post('/api/v1/participants/', response_model=participants.Participant_pydantic)
def create_participant(participant: participants.Participant_pydantic):
    existing_email = session.query(participants.Participant).filter_by(email=participant.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered.")

    existing_phone = session.query(participants.Participant).filter_by(phone=participant.phone).first()
    if existing_phone:
        raise HTTPException(status_code=400, detail="Phone number already registered.")

    participant = participants.Participant(**participant.dict())
    session.add(participant)
    session.commit()
    return participant
```
#### Explanation:
Adds a new participant to the database after validating email and phone uniqueness.

### 5. Get Event Details
#### Code:
```python
@app.get('/api/v1/events/{event_id}')
def read_event(event_id: int):
    event = session.query(events.Event).get(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found.")
    return event.to_dict()
```
#### Explanation:
Fetches details for a specific event by event ID.

### 6. Create Event
#### Code:
```python
@app.post('/api/v1/events/', response_model=events.Event_pydantic)
def create_event(event: events.Event_pydantic):
    event = events.Event(**event.dict())
    session.add(event)
    session.commit()
    return event
```
#### Explanation:
Adds a new event to the database.

---

## Running the API
To start the FastAPI server, use the following command:
```bash
fastapi dev .\api\main.py
```

---

## Deploying on Azure

### Step 1: Create an Azure Virtual Machine (VM)
1. Go to [Azure Portal](https://portal.azure.com/#home).
2. Create a new Virtual Machine (VM).
![image](https://github.com/user-attachments/assets/a3d6be16-85c4-4e17-ab8a-3efb0517de69)

![image](https://github.com/user-attachments/assets/52dff1c0-fe55-4865-a3fe-75d2a785a13a)


3. Follow the setup process and save the SSH key provided.

### Step 2: Connect to the VM
![image](https://github.com/user-attachments/assets/c792bfde-1e24-4afc-88f2-1b70295775dd)
![image](https://github.com/user-attachments/assets/f8a851f9-b34c-4f2a-aa1c-e537c67d25a0)


1. Open your terminal or command prompt.
2. Use the SSH key to connect to the VM:
   ```bash
   ssh -i path_to_your_key.pem username@vm_ip_address
   ```

### Step 3: Set Up the Environment on the VM
1. Clone the repository:
   ```bash
   git clone https://github.com/Hamza-Bouzoubaa/Build-DeployAPIs-Workshop-.git
   ```
2. Navigate to the project folder and activate the virtual environment:
   ```bash
   cd project_folder
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Step 4: Run the Web App and API
1. Start the Flask web app on the public IP:
   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```
2. Start the FastAPI app on the public IP:
   ```bash
   fastapi dev .\api\main.py  --host=0.0.0.0 --port=5000
   ```

### Step 5: Open Ports in Azure
1. Open ports `5000` and `8000` in the Azure VM network settings (Create two new inbound rules).
![image](https://github.com/user-attachments/assets/9fc78c22-3dfe-4382-89ca-eb732fcf972e)

2. Access the applications:
   - Web App: `http://vm_ip_address:5000`
   - API: `http://vm_ip_address:8000`

---

## Verification
1. Open your browser and navigate to:
   - `http://vm_ip_address:5000` to interact with the web app.
   - `http://vm_ip_address:8000` to interact with the API.
2. Test the endpoints using tools like Postman or cURL.


