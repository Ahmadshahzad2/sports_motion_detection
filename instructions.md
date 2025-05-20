# HomeTeam Network: AI Engineer Take-Home Project
## Sports Motion Detection & Viewport Tracking

### Project Overview
Implement a motion detection and viewport tracking system for sports video that identifies areas of activity and creates a smooth "virtual camera" view that follows the action. This project is designed to be completed in 2-3 hours and focuses on your Python skills, computer vision knowledge, and code organization.

### Task Description
Build a program that processes a short sports video clip to detect motion, track the primary action area, and create a smooth viewport that simulates professional camera operation. We've intentionally scoped this to be manageable while still demonstrating relevant skills.

### Project Requirements

#### 1. Video Processing
* Load and process a provided short sports video clip (10 seconds)
* Extract frames at a regular interval (e.g., 5 fps)
* Basic image preprocessing (resize to a standard resolution)

#### 2. Motion Detection
* Implement a simple frame differencing algorithm to detect motion
* Apply basic filtering to reduce noise
* Identify and prioritize significant movement areas

#### 3. Viewport Tracking
* Create a "virtual camera" viewport (a rectangle of fixed size, e.g., 720x480)
* Make the viewport track the main action area based on motion detection
* Implement basic smoothing to prevent jerky camera movements

#### 4. Results Visualization
* Create a visualization showing:
   * Original frame with detected motion areas (bounding boxes)
   * Viewport rectangle overlaid on the original frame
   * The cropped viewport view as a separate visualization
* Save the output as a series of images and a video

#### 5. Documentation
* Write clear comments in your code
* Create a README explaining:
   * How to run your code
   * Your approach and key design decisions
   * Challenges encountered and how you addressed them
   * Ideas for future improvements

### Project Materials
We will provide:
* A sample 10-second sports video clip
* A starter code template with basic utilities (optional to use)

### Evaluation Criteria
We will evaluate your submission based on:
1. **Code Quality**: Clean, readable code with appropriate organization
2. **Functionality**: Successfully detecting motion and tracking the action
3. **Algorithm Design**: How you implement viewport smoothing
4. **Documentation**: Clear explanation of your approach and design decisions
5. **Problem-Solving**: How you handle challenges like noise or multiple motion areas

### Submission Instructions
1. Create a private GitHub repository
2. Commit your code with clear commit messages
3. Include a README.md with your documentation
4. Share the repository with our GitHub account: `msvhsn-htn`

### Time Expectation
This project is designed to take 2-3 hours. We're looking for clean, functioning code rather than a perfect solution.

### Questions?
If you have any questions or need clarification, please email <hossein.moosavi@hometeamlive.com>.

Good luck, and we look forward to reviewing your submission!