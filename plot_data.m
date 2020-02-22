close all
clear
data = readtable('2_19_test.csv');
time_ranges = readtable('2_19_test_labels.csv','ReadRowNames',true);

time=table2array(data(:,'time'));
x=table2array(data(:,'x'));
y=table2array(data(:,'y'));
z=table2array(data(:,'z'));
us = table2array(data(:,'ultra_sonic'));
us = us - us(1);
us = us/200;

figure(420)
plot(us)

resting = 68:595;
test_2 = 596:2386;
test_3 = 2186:3880;
marissa_row_low = test_2(140:240);
marissa_row_mid = test_2(260:360);
marissa_row_high = test_2(385:485);
marissa_row_no_pause = test_2(510:610);
esther_row_low = test_2(720:940);
esther_row_mid = test_2(990:1190);
esther_row_high = test_2(1210:1380);
esther_row_no_pause = test_2(1440:1590);


figure(69)
plot(z(test_2))

intervals = {marissa_row_low, marissa_row_mid, marissa_row_high, marissa_row_no_pause, esther_row_low, esther_row_mid, esther_row_high, esther_row_no_pause};

figure(1)
hold on
plot(x)
plot(y)
plot(z)
legend({'x_acc','y_acc','z_acc'})

figure(2)
hold on
figure(3)
hold on
figure(4)
hold on

cutoff = 0.06;

for i = 1:4
    z_acc{i} = z(intervals{i})-mean(z(intervals{i}));
    z_acc{i} = wthresh(z_acc{i},'h', std(z_acc{i}));
    z_vel{i} = cumtrapz(time(intervals{i}), z_acc{i});
    z_pos{i} = cumtrapz(time(intervals{i}), z_vel{i});
    figure(2)
    plot(z_vel{i})
    figure(3)
    plot(z_pos{i})
    pos_low = lowpass(us, cutoff);
    pos_high = highpass(z_pos{i}, cutoff);
    pos_comp = pos_low(intervals{i}) + pos_high;
    figure(4)
    plot(pos_comp)
end

figure(5)
hold on
figure(6)
hold on
figure(7)
hold on

for i = 5:8
    z_acc{i} = z(intervals{i})-mean(z(intervals{i}));
    z_acc{i} = wthresh(z_acc{i},'h', std(z_acc{i}));
    z_vel{i} = cumtrapz(time(intervals{i}), z_acc{i});
    z_pos{i} = cumtrapz(time(intervals{i}), z_vel{i});
    figure(5)
    plot(z_vel{i})
    figure(6)
    plot(z_pos{i})
    pos_low = lowpass(us, cutoff);
    pos_high = highpass(z_pos{i}, cutoff);
    pos_comp = pos_low(intervals{i}) + pos_high;
    figure(7)
    plot(pos_comp)
end

figure(4)
title('Marissa Rows')
xlabel('samples')
ylabel('position (m)')
legend({'Too little', 'Good weight', 'Too much', 'no pauses'})

figure(7)
title('Esther Rows')
xlabel('samples')
ylabel('position (m)')
legend({'Too little', 'Good weight', 'Too much', 'no pauses'})
