%for T=[0.99, 0.95, 0.9, 0.85]
    T = 1.0
    n = 1000;
    rho = linspace(0.2, 2.0, n);
    p = zeros(1,n);
    V = zeros(1,n);
    g = zeros(1,n);
    for i = 1:n-1
        p(i) = 8*rho(i)*T/(3 - rho(i)) - 3*rho(i)^2;
        V(i) = 1/rho(i);
        g(i) = -3*rho(i) - 8.0/3.0*T*log(3.0/rho(i) - 1) + p(i)/rho(i);
    end
    [x0, y0, segments] = selfintersect(p, g);
    %x = [x0, x0];
    %y = [1.04248, 1.72706];
    plot(V, p)
    xlabel('Volume')
    ylabel('Pressure')
    %hold on
    %plot(y, x)
    legend({'T = 1.0'})
    
%end