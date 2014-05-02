BeagleBone Black回路実験 サンプルスクリプト

[「BeagleBoneBlack」で制御するロボットの作り方](http://www.amazon.co.jp/dp/4777518078)を参考にしたサンプルスクリプトです。

## test_makee.py

- I2Cデバイスである液晶パネルを使ったデモ
- HTMLのmarqueeのように文字が動きます
- スペルが違うのはご愛嬌

## firefly_led.py

- スイッチを押すとLEDが明滅
- 明滅の間隔をアナログ抵抗で制御
- 明滅の間隔を液晶パネルに表示
- スイッチと液晶パネルのオンオフが同期


