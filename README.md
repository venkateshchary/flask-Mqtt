<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="static/images/MQTT.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">MQTT integration with FLASK framework</h3>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Here's why:
* When the flask app is loaded it will connect to mqtt broker
* Terminating the app it will terminate the connection



### Built With

* [Python](https://www.python.org/)
* [MQTT](https://mosquitto.org/blog/2013/01/mosquitto-debian-repository/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

* python
  ```sh
    sudo apt install python3
    python3 -m venv venv
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/venkateshchary/Chalice-lambda-python.git
   ```
3. Install Python  packages
   ```sh
    source venv/bin/activate
    pip3 install -r requirements.txt
   ```
4. Create flask-mqtt app
   ```sh
    python3 flask_mqtt_wsgi.py
   ```
5. Test publisher and subscriber from cmd
    ```sh
        mosquitto_pub -t test_sender -m '{"name":"mqtt"}'
        mosquitto_sub -t test_receiver 
      ```
 

# License

Distributed under the MIT License. See `LICENSE` for more information.
