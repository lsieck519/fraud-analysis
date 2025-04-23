SELECT
    COUNT(*) AS total_orders,

    -- Country mismatches
    SUM(CASE WHEN issuer_country != billing_country THEN 1 ELSE 0 END) AS issuer_vs_billing_mismatch,
    SUM(CASE WHEN issuer_country != ip_country THEN 1 ELSE 0 END) AS issuer_vs_ip_mismatch,
    SUM(CASE WHEN billing_country != ip_country THEN 1 ELSE 0 END) AS billing_vs_ip_mismatch,

    -- Last-minute bookings
    SUM(CASE WHEN CAST("booking_days_before_checkin/departure" AS INTEGER) <= 1 THEN 1 ELSE 0 END) AS last_minute_bookings,

    -- One-way & international flights
    SUM(CASE WHEN flight_type = 'one_way' THEN 1 ELSE 0 END) AS one_way_flights,
    SUM(CASE WHEN flight_departure_country != flight_arrival_country THEN 1 ELSE 0 END) AS international_flights,

    -- High-value transactions
    SUM(CASE WHEN amount_usd > 1000 THEN 1 ELSE 0 END) AS high_value_orders

FROM fraud2;
