# Google Assistant Timer

Allows to send commands to Google Assistant that will execute after a certain time interval.

_Example:_

* _"Hey Google, turn off the light after 10 minutes"_
* _"Hey Google, turn on the fan for 25 minutes"_
* _"Hey Google, turn on/off `device` after `x` minutes"_

## How does it work?

**Google Assistant Timer** uses [IFTTT](https://ifttt.com/) to communicate with Google Assistant and your smart device.

## Installation

### Prerequisites

* Web Server that running Python
* [Python](https://www.python.org/) 3 or higher
* [IFTTT](https://ifttt.com/) account

#### Clone this repository

``` bash
git clone https://github.com/pizidavi/Google-Assistant-Timer.git
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

COMING SOON

---

## Running the app

Open the `main.py` file  

_or_

``` bash
# In command line
python3 main.py
```

## API Reference

### Usage

 `POST /trigger/<action>`

#### Request head

| Name | Type | Required | Description |
| :--- | :--- | :---| :--- |
| `action` | string  | **Yes**  | The action to execute. It can be **on** or **off** |

#### Request body

Content type: `application/json`

| Name | Type | Required | Description |
| :--- | :--- | :---| :--- |
| `key` | string  | **Yes**  | The Security Key specified in the server |
| `durationInMinutes` | number  | **Yes**  | Minutes to wait |
| `deviceName` | string  | **Yes**  | Name of the target device |
| `targetState` | boolean | No | The action to execute. _True_ -> Execute **after** X minutes, _False_ -> Execute **for** X minutes |

#### Example

Making a `POST` request with the parameters below will set the `light` to `ON` after `20` minutes.

URL: http://your-server.it/trigger/on

``` json
{
  "key": "XXXXX",
  "durationInMinutes": 20,
  "deviceName": "light",
  "targetState": false
}
```

## License

**Google Assistant Timer** is [MIT](LICENSE) licensed.  

## Credit

The idea of **Google Assistant Timer** come from [Time for Google Assistant](https://github.com/wiseindy/timer-for-google-assistant), because I tried to use the "original" one but I couldn't make it work :(  
So I have rewritten the code in Python.
