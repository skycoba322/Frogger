def proov(22):
    GPIO.output(valge, GPIO.HIGH)


GPIO.add_event_detect(channel, GPIO.RISING, callback=proov)


GPIO.output(punane, GPIO.HIGH)
GPIO.output(punejalg, GPIO.LOW)
GPIO.output(rohejalg, GPIO.HIGH)
time.sleep(5)
            
GPIO.output(rohejalg, GPIO.LOW)
GPIO.output(punejalg, GPIO.HIGH)
GPIO.output(kollane, GPIO.HIGH)
GPIO.output(punane, GPIO.LOW)
            time.sleep(1)
            
GPIO.output(kollane, GPIO.LOW)
GPIO.output(roheline, GPIO.HIGH)
time.sleep(5)
GPIO.output(roheline, GPIO.LOW)
vilkumine = 0
for i in range(3):
    GPIO.output(kollane, GPIO.HIGH)
    time.sleep(0.33)
    GPIO.output(kollane, GPIO.LOW)
    time.sleep(0.33)