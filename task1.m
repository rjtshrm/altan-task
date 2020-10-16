% list of all .mat files
f = {dir("/MATLAB Drive/Published/*.mat").name};

% iterate through all.mat files
for i_file = f
    % check column name with substr dut
    load(i_file{1})
    dut_col = contains(lower(tbl.Properties.VariableNames), 'dut'); % check which column has dut substring
    dut_col = find(dut_col, 1);
    % disp dut column
    disp(tbl(:, dut_col));
end


