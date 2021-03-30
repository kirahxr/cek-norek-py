# Cek Nomor Rekening

Cek nama pemilik nomor rekening

### URL
<https://api-v2.makira.id/cek-norek?bank={}&norek={}>

### Usage
```
Method: GET
Params: 
- bank = Kode Bank
- norek = Nomor Rekening
```
Daftar Kode Bank di Indonesia: <https://flip.id/kode-bank>

### Return
|err|message |Data  |date              |
|:--:|:-----:|:----:|:-------------------:|
|false |success|JSON  |datetime              |
|true |failed |  |datetime               |

### Author
<risky@makira.id>
