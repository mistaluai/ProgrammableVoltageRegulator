#include <Arduino.h>

const int pwm_pin = 9;
const int deadband = 0.2;

void setup() {
  // Set the PWM frequency to 1000 Hz.
  analogWriteFrequency(pwm_pin, 1000);
}

void loop() {
  // Read the output voltage of the buck converter.
  int output_voltage = analogRead(A0);

  // Calculate the difference between the output voltage and the desired output voltage.
  int difference = 12.0 - output_voltage;

  // Check if the difference between the output voltage and the desired output voltage is greater than the deadband.
  if (abs(difference) > deadband) {
    // Set the PWM duty cycle based on the difference between the output voltage and the desired output voltage.
    int pwm_duty_cycle = difference / 2.0;

    // Set the PWM duty cycle.
    analogWrite(pwm_pin, pwm_duty_cycle);
  }
}