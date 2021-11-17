## Foreign Pronunciation Generator  (English-Chinese)
![avatar](icon/icon.jpg)


We provide a simple socket script for acquiring Chinese pronunciation of English words (phones in ai-shell lexicon), in which the pronunciation generation algorithm uses ASR phoneme decoding and posterior analysis, with technical support provided by Qudra-V speech studio.

#### Notification:
updating
#### Usage and demo
    
    python generator.py <english_word>

take word "office" as example:

    python generator.py office

the remote server will show you some candidates in terminal:

    OFFICE aa ao4 f ei3 s iy3
    OFFICE aa ao4 f ei3 s iy5
    OFFICE aa ao4 f ei4 s iy5
    OFFICE aa ao4 f ei4 s iy3

This is a quick tool to solve code-switch speech recognition problems by adding the pronunciation to the lexicon of the monolingual ASR and modifying the language mode.
