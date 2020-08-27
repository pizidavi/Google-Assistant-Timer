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

* Web Server with Python (so that IFTTT can make requests to your server)
* [Python](https://www.python.org/) 3 or higher
* [IFTTT](https://ifttt.com/) account

### Clone this repository

``` bash
git clone https://github.com/wiseindy/timer-for-google-assistant.git
```

### Copy the `config.json.sample` in `config.json` and change the settings  

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
	* `KEY` : Get your IFTTT key from [IFTTT Service](https://ifttt.com/maker_webhooks). Click the **Documentation** button at the top right to get your key.  
	* `OFF_suffix` : The suffix for the "off" action in IFTTT.  
	* `ON_suffix` : The suffix for the "on" action in IFTTT.  

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

 `POST /trigger`

### Request body

Content type: `application/json`

| Name | Type | Required | Default value | Description |
| :--- | :--- | :---| :--- | :--- |
| `key` | string  | **Yes**  | - | This key can be any value, however, it should the match the key specified while setting up the server. |
| `durationInMinutes` | number  | **Yes**  | - | Number of minutes after which the action should be triggered. |
| `deviceName` | string  | **Yes**  | - | Name of the target device. |
| `targetState` | boolean | No       | false | What should the state of the device be *after* firing the event? `true` = ON; `false` = OFF |

#### Example

Making a `POST` request with the parameters below will set the `light` to `OFF` after `20` minutes.

``` json
{
  "key": "XXXXX",
  "durationInMinutes": 20,
  "deviceName": "light",
  "targetState": false
}
```

#### A note on the `targetState` parameter

If `targetState` is set to `false` (i.e., OFF), the device will be first turned `ON` upon receiving this command. After the specified time has elapsed, the device will be turned `OFF`. This is an optional parameter and by default, `targetState` is `false`.  
If `targetState` is set to `true` (i.e., ON), it will do the opposite. The device will be first turned `OFF` upon receiving this command. After the specified time has elapsed, the device will be turned `ON`.  


## License

**Google Assistant Timer** is [MIT](LICENSE) licensed.  
All trademarks are the property of their respective owners.  
