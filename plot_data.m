close all
data = readtable('2_19_test.csv');
time_ranges = readtable('2_19_test_labels.csv','ReadRowNames',true);

time=table2array(data(:,'time'));
x=table2array(data(:,'x'));
y=table2array(data(:,'y'));
z=table2array(data(:,'z'));

resting = 68:595;
test_2 = 596:2185;
test_3 = 2186:3880;
marissa_row_low = 140:240;
marissa_row_mid = 260:360;
marissa_row_high = 385:485;
marissa_row_no_pause = 510:595;

figure()
hold on
plot(x(test_2))
plot(y(test_2))
plot(z(test_2))
legend({'x_acc','y_acc','z_acc'})

z_acc_1 = z(marissa_row_low)-mean(z(marissa_row_low));
z_acc_1 = wthresh(z_acc_1,'h', std(z_acc_1));
z_vel_1 = cumtrapz(time(marissa_row_low), z_acc_1);
z_pos_1 = cumtrapz(time(marissa_row_low), z_vel_1);

z_acc_2 = z(marissa_row_mid)-mean(z(marissa_row_mid));
z_acc_2 = wthresh(z_acc_2,'h', std(z_acc_2));
z_vel_2 = cumtrapz(time(marissa_row_mid), z_acc_2);
z_pos_2 = cumtrapz(time(marissa_row_mid), z_vel_2);

z_acc_3 = z(marissa_row_high)-mean(z(marissa_row_high));
z_acc_3 = wthresh(z_acc_3,'h', std(z_acc_3));
z_vel_3 = cumtrapz(time(marissa_row_high), z_acc_3);
z_pos_3 = cumtrapz(time(marissa_row_high), z_vel_3);

z_acc_4 = z(marissa_row_no_pause)-mean(z(marissa_row_no_pause));
z_acc_4 = wthresh(z_acc_4,'h', std(z_acc_4));
z_vel_4 = cumtrapz(time(marissa_row_no_pause), z_acc_4);
z_pos_4 = cumtrapz(time(marissa_row_no_pause), z_vel_4);


figure()
hold on
plot(z_vel_1)
plot(z_vel_2)
plot(z_vel_3)
plot(-z_vel_4)
title('Marissa row velocity')
xlabel('samples (2Hz)')
ylabel('velocity (m/s)')
legend({'Too little', 'Good weight', 'Too much', 'no pauses'})

figure()
hold on
plot(z_pos_1)
plot(z_pos_2)
plot(z_pos_3)
plot(-z_pos_4)
title('Marissa row position')
xlabel('samples (2Hz)')
ylabel('displacement (m)')
legend({'Too little', 'Good weight', 'Too much', 'no pauses'})