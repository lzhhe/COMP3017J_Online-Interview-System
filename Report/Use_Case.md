---

**System Name:** Online Interview System

---

**1. Use Case Name:** Log in

**Actor:** Candidate, Interviewer

**Brief Description:** The actor logs into the Online Interview System.

**Preconditions:** The actor has already registered an account.

**Main Flow:**
1. Actor enters username and password.
2. System validates the credentials.
3. System grants access and lets the actor enter the platform.

**Alternate Flow:**
- 2a. If the credentials are invalid, the system displays an error message.

---

**2. Use Case Name:** Create Account

**Actor:** Candidate, Interviewer

**Brief Description:** The actor registers a new account on the Online Interview System.

**Preconditions:** None

**Main Flow:**
1. Actor provides necessary registration details (e.g., name, email, password).
2. System verifies the input.
3. System confirms the creation of the new account.

**Alternate Flow:**
- 2a. If the provided details are invalid or already exist, the system displays an error message.

---

**3. Use Case Name:** Write Code

**Actor:** Candidate, Interviewer

**Brief Description:** The actor writes code in the browser-based IDE.

**Preconditions:** Actor is logged in.

**Main Flow:**
1. Actor inputs code in the IDE.
2. Actor has the option to save or run the code.

---

**4. Use Case Name:** Run Code

**Actor:** Candidate, Interviewer

**Brief Description:** The actor executes the code they wrote.

**Preconditions:** Actor has written code.

**Main Flow:**
1. Actor clicks on the "Run" button.
2. System executes the code and displays the result.

---

**5. Use Case Name:** Choose Language

**Actor:** Candidate, Interviewer

**Brief Description:** The actor selects a programming language.

**Preconditions:** Actor is logged in and is on the IDE.

**Main Flow:**
1. Actor selects the required programming language from a dropdown menu.
2. System configures the IDE based on the selected language.

---

**6. Use Case Name:** Debug Code

**Actor:** Candidate, Interviewer

**Brief Description:** The actor debugs the code they wrote, identifying and fixing errors.

**Preconditions:** Actor has written code.

**Main Flow:**
1. Actor sets breakpoints in the IDE.
2. Actor clicks on the "Debug" button.
3. System pauses execution at the breakpoints and displays the current value of variables.

---

**7. Use Case Name:** Communicate Online

**Actor:** Candidate, Interviewer

**Brief Description:** The actor communicates with another participant through online chat.

**Preconditions:** Both participants are logged in.

**Main Flow:**
1. One participant sends a message.
2. The other participant receives and replies to the message.

---

**8. Use Case Name:** Communicate In Video

**Actor:** Candidate, Interviewer

**Brief Description:** The actor engages in a video conversation with another participant.

**Preconditions:** Both participants are logged in and have their cameras and microphones connected.

**Main Flow:**
1. One participant initiates the video call.
2. The other participant accepts and the video conversation begins.

---

**9. Use Case Name:** Communicate In Audio

**Actor:** Candidate, Interviewer

**Brief Description:** The actor engages in an audio conversation with another participant.

**Preconditions:** Both participants are logged in and have their microphones connected.

**Main Flow:**
1. One participant initiates the audio call.
2. The other participant accepts and the audio conversation begins.

---

**10. Use Case Name:** Manage Interviews

**Actor:** Interviewer

**Brief Description:** The interviewer schedules and manages interviews.

**Preconditions:** Interviewer is logged in.

**Main Flow:**
1. Interviewer views a list of candidates to be interviewed.
2. Interviewer schedules or reschedules interview timings.
3. Interviewer sends interview invites to candidates.

---

**11. Use Case Name:** Evaluate Code

**Actor:** Interviewer

**Brief Description:** The interviewer evaluates the code written by the candidate.

**Preconditions:** Interviewer is logged in; Candidate has completed code writing.

**Main Flow:**
1. Interviewer reviews the code submitted by the candidate.
2. Interviewer runs the code and checks the results.
3. Interviewer provides feedback and evaluations of the code.

---

**12. Use Case Name:** Draw on Whiteboard

**Actor:** Candidate, Interviewer

**Brief Description:** The participants use a virtual whiteboard for technical visual communication.

**Preconditions:** Both participants are logged in.

**Main Flow:**
1. One participant starts drawing on the whiteboard.
2. The other participant sees the drawing in real-time and can interact or add content.

---

**13. Use Case Name:** Review Records

**Actor:** Candidate, Interviewer

**Brief Description:** The interviewer reviews past interview records.

**Preconditions:** Interviewer is logged in.

**Main Flow:**
1. Interviewer selects an interview record to review.
2. System displays detailed records of the selected interview, including interactions, evaluations, and feedback.
