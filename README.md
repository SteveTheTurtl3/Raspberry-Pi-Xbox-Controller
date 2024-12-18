

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://cekcreator/RaspberryPi_XboxController">
  </a>

<h3 align="center">RaspberryPi_XboxController</h3>

  <p align="center">
    This project leverages the power of a Raspberry Pi, Python programming, and the evdev library to create a wireless control interface for a soldering machine using an Xbox controller.
  </p>
    <p>
    This is a project my brother and I worked on for a local machining company.
    </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project

The aim of this project is to enable users to remotely control a soldering machine from a distance using an Xbox controller. By interfacing the Xbox controller with the Raspberry Pi and implementing a button-to-action mapping, the soldering machine's functions can be conveniently controlled without direct physical access.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* 1x Raspberry SC15184 Pi 4 Model B 2019 Quad Core 64 Bit WiFi Bluetooth (2GB)
* 1x Raspberry Pi 32GB Preloaded (NOOBS) SD Card
* 1x 400 Point Solderless Breadboard
* 20x 10cm male to female jumper wires
* 20x 20cm male to male jumper wires
* 10x 330 Ohm Resistors, 1/2 W, 5%
* 1x battery pihat w/ extra accessories
* 1x Xbox Knockoff Wireless Controller
* 10x 5mm LED Light Diodes
* 1x Wireless Keyboard and Mouse
* 1x 15W USB-C Power Supply
* 1x SD Card to USB C Reader
* 1x Micro HDMI to HDMI Cable
* 1x metal case for raspi w/ fan

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Files
* SendPowerViaButtons.py: The heart of the project, this Python script translates Xbox controller inputs into signals that control the soldering machine. It handles the button presses and sends corresponding commands to the machine's functions.

* gamepad.py: A utility script used during development to identify Xbox controller button event codes and names. This assisted in accurately mapping controller inputs to soldering machine actions.

* LED.py: A testing script to validate LED functionality. This script ensures that LED indicators respond as expected, confirming successful communication between the Raspberry Pi and the hardware components.

* evtest.py: This script lists all connected input devices, aiding in identifying the name of the connected Xbox controller. The accurate device name is crucial for the evdev library to communicate with the controller effectively.

<!-- LICENSE -->
## License

* Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

* Talia Kumar - https://www.linkedin.com/in/talia-kumar-83b948279/ - talia_kumar@mines.edu
* Caleb Kumar - https://www.linkedin.com/in/caleb-k-0232b719b/ - caleb.kumar@colorado.edu

* Project Link: [https://cekcreator/RaspberryPi_XboxController](https://cekcreator/RaspberryPi_XboxController)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

	* [Talia Kumar]()
* [Caleb Kumar]()


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/githcekcreator/RaspberryPi_XboxController.svg?style=for-the-badge
[license-url]: https://cekcreator/RaspberryPi_XboxController/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/caleb-k-0232b719b/
