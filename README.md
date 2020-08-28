# Google Assistant Timer

Allows to send commands to Google Assistant that will execute after a certain time interval.

_Example:_

* _"Hey Google, turn on the light after 5 minutes"_
* _"Hey Google, turn on the fan for 25 minutes"_
* _"Hey Google, turn on/off `device` after `x` minutes"_

## How does it work?

**Google Assistant Timer** uses [IFTTT](https://ifttt.com/) to communicate with Google Assistant and your smart device.

## Installation

### Prerequisites

* Web Server Linux that running Python ([Heroku](https://www.heroku.com/) is a free option)
* [Python](https://www.python.org/) 3 or higher
  * Python WSGI (like [Gunicorn](https://gunicorn.org/))
* [IFTTT](https://ifttt.com/) account

#### Clone this repository

``` bash
git clone https://github.com/pizidavi/Google-Assistant-Timer.git
```

#### Install requirements

``` bash
cd Google-Assistant-Timer
pip install -r requirements.txt
```

_or_

``` bash
cd Google-Assistant-Timer
python -m pip install -r requirements.txt
```

#### Copy the `config.json.sample` in `config.json` and change the settings  

``` json
{
  "SECURITY_KEY": "SECURITY_KEY",
  "IFTTT": {
    "KEY": "IFTTT_KEY",
    "OFF_suffix": "_off",
    "ON_suffix": "_on"
  }
}
```

* `SECURITY_KEY` : Set this to a **unique** string.  
* `IFTTT`  
	* `KEY` : Get your key from [IFTTT Service](https://ifttt.com/maker_webhooks) clicking the *Documentation* button at the top right.  
	* `OFF_suffix` : The suffix for the "off" action.  
	* `ON_suffix` : The suffix for the "on" action.  

---

### Integrate with IFTTT

In IFTTT two actions are created: one to _turn the device off_ and another to _turn it on_.

#### Set up IFTTT Webhooks

1. Login to your [IFTTT](https://ifttt.com/) and create a new applet. For the `this` trigger, choose `Webhooks`  
2. Follow a consistent naming scheme for all events. Use the correct suffixes for your device events as specified in the `OFF_suffix` and `ON_suffix` parameters in the `config.json` file  
\
For example, if the device is a smart light, use `light_off` and `light_on` as the event names to turn the light OFF and ON respectively.
\
**Make sure you follow the SAME naming scheme for ALL events (they're case sensitive)**  

3. Next, choose your smart device from the list and select the action you'd like to carry out  
4. Repeat the above steps to create the other trigger  

#### Configure IFTTT to receive commands from Google Assistant and forward to your server

1. Create a new applet/action in IFTTT. For the `this` trigger, choose `Google Assistant`  
2. Select: **Say a phrase with a number**  
3. Set your trigger phrase and the response. Use `#` to specify where you'll say the number of minutes
\
In this example, I want Google Assistant to turn on the light and then turn it off after X minutes.  

5. For the `that` action in your applet, select `Webhooks`  
6. Fill the action fields with the following values
\
For the `URL` field, type in the domain/IP of your webserver running this application.\
The API endpoint that handles requests is `/trigger`.\
Set the web request method to `POST`.\
Select `application/json` as Content Type.

For the Body parameter, specify the following values:  
_Sample request body:_

```
{
  "key": "SECURITY_KEY",
  "durationInMinutes": {{NumberField}},
  "deviceName": "light",
  "targetState": false
}
```

* Make sure to use the same `key` that you specified in the `config.json` file.
* The device name `light` should match the name used to create OFF/ON events: `light_off` and `light_on`. These values are **case-sensitive**.  

For more information, refer to the [API Reference](#api-reference) below  

---

## Running the app

### Production

``` bash
gunicorn -w 4 main:app
```

### Development

Open the `main.py` file  

_or_

``` bash
python main.py
```

## API Reference

### Usage

`POST /trigger`

#### Request body

Content type: `application/json`

| Name | Type | Required | Default | Description |
| :--- | :--- | :---| :--- | :--- |
| `key` | string  | **Yes**  |  | The Security Key specified in the config file |
| `durationInMinutes` | number  | **Yes** |  | Minutes to wait |
| `deviceName` | string  | **Yes** |  | Name of the device |
| `targetState` | boolean | No | False | The status of the device after the event has been fired |

#### Example

Set the _light_ to `ON` after 2 minutes.  

POST Request to http://your-server.it/trigger  

``` json
{
  "key": "Same as the configuration file",
  "durationInMinutes": 2,
  "deviceName": "light",
  "targetState": true
}
```

## License

**Google Assistant Timer** is [MIT](LICENSE) licensed.  

## Credit

The idea of **Google Assistant Timer** come from [Time for Google Assistant](https://github.com/wiseindy/timer-for-google-assistant), because I tried to use the "original" one but I couldn't make it work.  
So I have rewritten the code in Python :)
