

function LL = cal_MNL_LL(beta,data)
    %data=evalin('base','data');  % load data
    LL=0;
    test_data_userId=unique(data(:,1));
    for index = 1:length(test_data_userId)
        i=test_data_userId(index);%当前srch id
        query_data=data(data(:,1)==i,:);
        if sum(query_data(:,8))>0
            click_data = query_data(query_data(:,8)==1,:); % find the click data
            temp1 = click_data(1,2:7)*beta;
            temp2 = log(1 +sum(exp(query_data(:,2:7)*beta)));
            LL=LL+temp1-temp2;   
        else
            LL=LL-log(1 +sum(exp(query_data(:,2:7)*beta)));
        end
    end
    LL = -LL/length(test_data_userId);
end
