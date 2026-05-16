# STT MODULE Issue LOG (Recording-wise)

Use this for 5-10 sample recordings. Keep entries short with issue IDs.

## 1) Issue Codebook

| ID  | Issue              | Cat      | Sev | Quick Note-> Under Evaluation |
| --- | ------------------ | -------- | --: | ----------------------------- |
| I01 | Hallucination      | Content  |   3 | Text not present in audio     |
| I02 | Over-segmentation  | Seg      |   2 | Split on breath/short pause   |
| I03 | Missed words       | Content  |   3 | Audible words missing         |
| I04 | Code-switch error  | Lang     |   2 | Hinglish/mix switching wrong  |
| I05 | Indic mis-class    | Lang     |   2 | Wrong language tag            |
| I06 | Phonetic confusion | Acoustic |   2 | Similar sounding word subbed  |
| I07 | Timestamp drift    | Timing   |   3 | Start/end times misaligned    |
| I08 | Pause handling     | Timing   |   2 | Pause added/removed wrongly   |
| I09 | Silence issue      | Pipeline |   2 | Silence transcribed/cut badly |
| I10 | List vs Gen        | Pipeline |   3 | Output mismatch (List vs Gen) |


##  Score Rule (quick)

Score = sum of `(Sev x count)` for that recording.

## 3) Recording Log

Format for `Issues (ID x count)`: `I02x3, I07x1`

|   # | Date        | Recording     | Mode | Issues (ID x count)        | Score | Notes (Max 10 words)                            | Status |
| --: | ----------- | ------------- | ---- | -------------------------- | ----: | ----------------------------------------------- | ------ |
|   1 | 22 March 26 | Test10_30.wav | List | I01x1, I05x1, I03x1, I07x1 |    11 | Hallucination & time stamps                     | open   |
|   2 | 22 March 26 | Test10_30     | Gen  | I05x1, I03x1,              |     5 | Sentence missing & no hindi, ubless mentioned   |        |
|   3 | 22 March 26 | Test4_15.wav  | List | 0                          |     0 | No issues, Yt English record.                   | close  |
|   4 | 1 April 26  | Test6_35.wav  | List | I0(1,3,6,7,etc)            |   INF | Saaransh clip -> Anarchy                        | open   |
|   5 | 22 March 26 | Test6_35.wav  | Gen  | I0(...)                    |       | 12s baad hi phus😒, still somewhat correct     | open   |
|   6 | 22 March 26 | Test7_25.wav  | List | I06x2, I09x1(maybe)        |   4+2 | Satisfactory job (pure Hindi emotional content) | close  |
|   7 | 22 March 26 | Test7_25.wav  | Gen  | I06x2, I09x1(maybe)        |   4+2 | Quick,Ovr Same                                  | close  |
|   8 | 22 March 26 | Test10_60.wav | List |                            |       | Cheete ki chaal, Very Tough                     |        |
|   9 | 22 March 26 | Test10_60.wav | Gen  |                            |       |                                                 |        |
|  10 | 22 March 26 | Final01_60    | List |                            |       |                                                 | open   |
|  11 | 22 March 26 | Final01_60    | Gen  |                            |       |                                                 | open   |
|     |             |               |      |                            |       |                                                 |        |


