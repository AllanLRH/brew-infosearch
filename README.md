# brew-infosearch

Show the result of `brew TAPNAME info` for all search results in tapped taps, and show the search result of untapped taps.

Add to path as `brew-infosearch`. Usage: `brew infosearch package_to_search_for`.


### Example output:

```
$ brew infosearch arduino

adafruit-arduino: 1.6.4
Adafruit Arduino
https://adafruit.com
Not installed
https://github.com/caskroom/homebrew-cask/blob/master/Casks/adafruit-arduino.rb
==> Contents
  Arduino.app (app)

≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈

arduino: 1.6.8
Arduino
https://www.arduino.cc/
Not installed
https://github.com/caskroom/homebrew-cask/blob/master/Casks/arduino.rb
==> Contents
  Arduino.app (app)
  Arduino.app/Contents/Java/arduino-builder (binary)
==> Caveats
arduino requires Java. You can install the latest version with

  brew cask install java

Cask arduino installs files under "/usr/local".  The presence of such
files can cause warnings when running "brew doctor", which is considered
to be a bug in homebrew-cask.


≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈

galileo-arduino: 1.5.3
Intel Galileo Arduino SW
https://communities.intel.com/docs/DOC-22226
Not installed
https://github.com/caskroom/homebrew-cask/blob/master/Casks/galileo-arduino.rb
==> Contents
  Arduino.app (app)


≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
The following results were found in untapped taps:

    Caskroom/versions/arduino-nightly
```
