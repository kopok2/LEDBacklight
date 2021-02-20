#include <stdio.h>
#include <math.h>

double logistic_regression_response (double linear_combination) {
    return 1.0 / (1.0 + exp(-linear_combination));
}

double calculate_linear_combination (double first_part[], double second_part[], int combination_length) {
    double result = 0.0;
    for (int i = 0; i < combination_length; i++) {
        result += first_part[i] * second_part[i];
    }
    return result;
}

int logistic_regression_decision (double observations[], double parameters[], double intercept, int parameters_length, double threshold) {
    double linear_combination = intercept;
    linear_combination += calculate_linear_combination(observations, parameters, parameters_length);
    double output = logistic_regression_response(linear_combination);
    printf("%f\n", output);
    return output > threshold;
}

double std_dev1(double a[], int n) {
    if(n == 0)
        return 0.0;
    double sum = 0;
    for(int i = 0; i < n; ++i)
       sum += a[i];
    double mean = sum / n;
    double sq_diff_sum = 0;
    for(int i = 0; i < n; ++i) {
       double diff = a[i] - mean;
       sq_diff_sum += diff * diff;
    }
    double variance = sq_diff_sum / n;
    return sqrt(variance);
}


int main () {
    FILE *myFile;
    myFile = fopen("plain.txt", "r");
    if (myFile == NULL)
    {
        printf("Can't open file for reading.\n");
    }

    double on_model_parameters[] = {-0.41624938,  0.41212599, -0.04200694, -0.15245494,  0.19430454,  0.22582816,
   0.56097061,  0.0815576,   0.01920004,  0.49723097, -0.37569262,  0.12507564,
  -0.21171196, -0.87159269, -0.05628933,  0.35996005, -0.13784693, -0.5079509};
    double on_model_intercept = -1.50597366;
    double off_model_parameters[] = {-0.1676783976042788, -0.07490376386931438, 0.1679468741641528, 0.20543775361618735,
             0.17936835589663927, -0.4774662932996938, -0.6803555471988786, -0.13736468551300987, 0.3642389901822257,
             0.12545928823219152, -0.3393245258375251, 0.22316485676210265,
             0.48307983581723346, 0.258810779369491, -0.1365470275428234, 0.031131370067844766, 0.0008176580329774881, -1.043453152345807};
    double off_model_intercept = -4.16206442;
    int parameters_length = 17;
    double threshold = 0.5;

    double window[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    double frame[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int window_length = 15;
    int cooldown = 0;
    int cooldown_setting = 74;
    int is_on = 0;
    int decision;

    for (int i = 0; i < 2607; i++) {
        // Shift window
        for (int j = 1; j < window_length; j++) {
            window[j - 1] = window[j];
        }
        // Get reading
        int reading;
        fscanf(myFile, "%d", &reading);
        window[window_length - 1] = reading;
        printf("%d\n", reading);
        // Prepare frame
        for (int j = 0; j < window_length; j++) {
            frame[j] = window[j];
        }
        frame[window_length] = frame[window_length - 1] - frame[0];
        frame[window_length + 1] = frame[window_length - 1] - frame[7];
        frame[window_length + 2] = std_dev1(window, window_length);
        if(cooldown == 0) {
            if(i > window_length) {
                if(is_on) {
                    decision = logistic_regression_decision(frame, on_model_parameters, on_model_intercept, parameters_length, threshold);
                } else {
                    decision = logistic_regression_decision(frame, off_model_parameters, off_model_intercept, parameters_length, threshold);
                }
                if(decision) {
                    printf("Switching state from %d\n", is_on);
                    is_on = !is_on;
                    cooldown = cooldown_setting;
                }
            }

        } else {
            cooldown--;
        }
    }



    return 0;
}
