CREATE TABLE jackpot_log (
    id          BIGINT PRIMARY KEY,
    state       CHAR(2) NOT NULL,
    linked_node BIGINT[],
    hit_amt     BIGINT DEFAULT NULL,
    hit_node    BIGINT DEFAULT NULL,
    hit_seq     BIGINT DEFAULT NULL,
    hit_time    TIMESTAMP DEFAULT NULL
)

