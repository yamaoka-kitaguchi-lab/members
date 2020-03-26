# メンバー管理リポジトリ [![Build Status](https://travis-ci.org/yamaoka-kitaguchi-lab/members.svg?branch=master)](https://travis-ci.org/yamaoka-kitaguchi-lab/members) ![validator](https://github.com/yamaoka-kitaguchi-lab/members/workflows/validator/badge.svg) [![Issues](https://img.shields.io/github/issues/yamaoka-kitaguchi-lab/members)](https://github.com/yamaoka-kitaguchi-lab/members/issues) [![PR](https://img.shields.io/github/issues-pr/yamaoka-kitaguchi-lab/members)](https://github.com/yamaoka-kitaguchi-lab/members/pulls)
研究室のメンバー（教員・学部学生・大学院生・留学生・卒業生）を管理するリポジトリです．
1. masterブランチのJSONファイルは[メンバーページ](https://www.net.ict.e.titech.ac.jp/members/)からJavascript経由で動的に参照されます
1. masterブランチは保護されており，ローカルの変更を反映するにはプルリクエストを作成する必要があります
1. プルリクエスト作成時に自動で構文チェックが実行され，これに成功した場合のみマージすることができます

## 各JSONファイルの目的
メンバーの更新時に編集が必要となるJSONファイルを説明します．  

### members.json
それぞれのrole（教職員・学生・交換留学生）にメンバーを追加していきます．

- *name*: 氏名です．姓と名の間には半角スペースを入れます
- *grade*: 学年です
- *account*: メールアドレスのアカウント名です
- *room*: デスクのある学生室です

```
  {
    "name": {"ja": "東工 太郎", "en": "Taro TOUKOU"},
    "grade": {"ja": "学部4年", "en": "B4"},
    "account": "toukou",
    "room": "S3-313"
  }
```

末尾カンマ（ケツカンマ）に注意してください．  
**最後のエントリはカギ括弧末尾にカンマをつけてはいけません．**

```
[
  {
    ...
  },
  {
    ...
  },
  {
    ...
  }
]
```

### past_students.json
卒業生（留学生除く）を追加していきます．

- *name*: 氏名です．姓と名の間には半角スペースを入れます
- *date*: 卒業年月です．2016年3月，2016年9月など
- *degree*: 取得学位です

```
  {
    "name": {"ja": "東工 太郎", "en": "Taro TOUKOU"},
    "date": {"ja": "2016年3月", "en": "Mar., 2016"},
    "room": {"ja": "学士（工学）", "en": "Bachelor of Engineering"}
  }
```

### past_exchange_students.json
研究室を去った留学生を追加していきます．

- *name*: 氏名です．姓と名の間には半角スペースを入れます
- *period*: 当研究室の在籍期間です
- *affiliation*: もとの所属機関名です
- *program*: 配属の根拠となった留学プログラム名です

```
  {
    "name": {"ja": "ジョン テック", "en": "John TECH"},
    "period": {"ja": "2016年3月から8月", "en": "Mar.2016 - Aug.2016"},
    "affiliation": {"ja": "フィズバズ工科大学", "en": "FizzBuzz Institute of Technology"},
    "program": {"ja": "ジョン・ドゥ・プログラム", "en": "John Doe Program"}
  }
```
