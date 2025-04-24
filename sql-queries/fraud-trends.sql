select
    count(*) as total_orders,

    -- country mismatches
    sum(case when issuer_country != billing_country then 1 else 0 end) as issuer_vs_billing_mismatch,
    sum(case when issuer_country != ip_country then 1 else 0 end) as issuer_vs_ip_mismatch,
    sum(case when billing_country != ip_country then 1 else 0 end) as billing_vs_ip_mismatch,

    -- last-minute bookings
    sum(case when cast("booking_days_before_checkin/departure" as integer) <= 1 then 1 else 0 end) as last_minute_bookings,

    -- high-value transactions
    sum(case when amount_usd > 5000 then 1 else 0 end) as high_value_orders,
    -- low-value transactions
    sum(case when amount_usd < 10 then 1 else 0 end) as low_value_orders

from fraud2;
