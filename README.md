# m5stickv-tips
M5StickV、UnitV用の色々なプログラム
※終了処理が無いなどまだ不完全です。

## 使い方
boot.pyにコピペして使ってください。

## Contents

### batterymonitor.py
バッテリーやUSBの電圧等を表示します。
※ファームウェア0.4.0_17以上で動作します。

### button.py
ボタンの値が関数でどう渡されるかを確認するためのサンプル

### button_unitv.py
UnitVのボタンの動作を確認するためのサンプル。
※１.動作にはws2812のmoduleがONになったファームウェアが必要です。ファームウェアのビルド方法は下記を見てください。
[M5StickVのファームウェアビルド手順](https://raspberrypi.mongonta.com/howto-build-firmware-of-m5stickv/)

※２.
moduleのlcdに関連するコメントを外すと常に0になります。これはUnitVのGPIO18,19がM5StickVのLCDが18,19と重なっているためです。M5StickVとUnitVで共通のソースを利用する場合は注意しましょう。
