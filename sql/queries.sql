CREATE DATABASE IF NOT EXISTS sla_dashboard;
USE sla_dashboard;

CREATE TABLE IF NOT EXISTS tickets (
    ticket_id VARCHAR(10),
    created_at DATETIME,
    first_response_at DATETIME,
    resolved_at DATETIME,
    priority VARCHAR(2),
    category VARCHAR(50),
    assignee_id VARCHAR(10),
    status VARCHAR(20)
);

INSERT INTO tickets VALUES
('T001','2026-09-01 09:00','2026-09-01 09:30','2026-09-01 16:00','P1','Network','A101','Resolved'),
('T002','2026-09-01 10:00','2026-09-01 12:00','2026-09-02 08:00','P2','Hardware','A102','Resolved'),
('T003','2026-09-01 11:00','2026-09-01 18:00',NULL,'P3','Software','A103','Open'),
('T004','2026-09-01 12:00','2026-09-01 13:00','2026-09-02 10:00','P4','Password','A101','Resolved'),
('T005','2026-09-01 13:00','2026-09-01 17:00',NULL,'P2','Network','A102','Open'),
('T006','2026-09-02 09:00','2026-09-02 09:20','2026-09-02 14:00','P1','Software','A103','Resolved'),
('T007','2026-09-02 10:00','2026-09-02 15:00','2026-09-03 12:00','P3','Hardware','A104','Resolved'),
('T008','2026-09-02 11:00','2026-09-02 11:30','2026-09-02 18:00','P4','Network','A101','Resolved'),
('T009','2026-09-02 13:00','2026-09-02 16:00',NULL,'P2','Software','A102','Open'),
('T010','2026-09-02 14:00','2026-09-02 15:00','2026-09-03 09:00','P3','Password','A104','Resolved');

SELECT * FROM tickets;
SELECT ticket_id, priority, status FROM tickets;
SELECT * FROM tickets WHERE priority = 'P1';
SELECT * FROM tickets WHERE status = 'Open';
SELECT COUNT(*) AS total_tickets FROM tickets;
SELECT priority, COUNT(*) AS ticket_count FROM tickets GROUP BY priority;
SELECT category, COUNT(*) AS ticket_count FROM tickets GROUP BY category ORDER BY ticket_count DESC;
SELECT status, COUNT(*) AS ticket_count FROM tickets GROUP BY status;
SELECT * FROM tickets WHERE resolved_at IS NULL;
SELECT assignee_id, COUNT(*) AS ticket_count FROM tickets GROUP BY assignee_id ORDER BY ticket_count DESC;