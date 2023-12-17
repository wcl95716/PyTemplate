-- 创建表格
CREATE TABLE IF NOT EXISTS ticket (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    key_id VARCHAR(100),
    status INT,
    priority INT,
    type INT,
    title TEXT,
    content TEXT,
    assigned_to_id VARCHAR(100),
    creator_id VARCHAR(100),
    create_time DATETIME,
    update_time DATETIME
);

-- 插入数据
-- 插入数据，其中 key_id 字段为空
INSERT INTO ticket ( status, priority, type, title, content, assigned_to_id, creator_id, create_time, update_time)
VALUES 
    ( 1, 1, 1, 'test1', 'content1', '1', '1', '2020-01-01 00:00:00', '2020-01-01 00:00:00'),
    ( 2, 1, 1, 'test2', 'content2', '2', '2', '2020-01-01 00:00:00', '2020-01-01 00:00:00'),
    (3, 1, 1, 'test3', 'content3', '3', '3', '2020-01-01 00:00:00', '2020-01-01 00:00:00');




