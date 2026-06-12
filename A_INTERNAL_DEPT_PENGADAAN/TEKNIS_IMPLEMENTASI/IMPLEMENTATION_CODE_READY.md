# AI PROCEDURE COMPLIANCE GUARDIAN - IMPLEMENTATION CODE
## Ready-to-Code Package for IT Team

---

## PART 1: DATABASE SCHEMA

```sql
-- ============================================
-- AI PROCEDURE COMPLIANCE GUARDIAN DATABASE
-- ============================================

-- 1. Document Repository
CREATE TABLE sop_documents (
  id SERIAL PRIMARY KEY,
  doc_id VARCHAR(50) UNIQUE,              -- DOC-001, DOC-002
  doc_name VARCHAR(255) NOT NULL,
  doc_type VARCHAR(50),                   -- pdf, docx, xlsx, txt
  file_path VARCHAR(500),
  file_size BIGINT,
  
  category VARCHAR(100),                  -- Procurement, Finance, HR
  version VARCHAR(20),                    -- 1.0, 2.1
  effective_date DATE,
  owner_id INT REFERENCES users(id),
  
  extraction_status VARCHAR(50),          -- pending, processing, completed, failed
  extraction_date TIMESTAMP,
  extraction_confidence DECIMAL(3,2),     -- 0.00-1.00
  
  doc_embedding VECTOR(1536),             -- OpenAI embedding
  doc_summary TEXT,                       -- AI-generated summary
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  CONSTRAINT extraction_confidence_range CHECK (extraction_confidence >= 0 AND extraction_confidence <= 1)
);

CREATE INDEX idx_sop_documents_category ON sop_documents(category);
CREATE INDEX idx_sop_documents_status ON sop_documents(extraction_status);
CREATE INDEX idx_sop_documents_embedding ON sop_documents USING ivfflat(doc_embedding);

-- 2. Procedures Knowledge Base
CREATE TABLE procedures (
  id SERIAL PRIMARY KEY,
  sop_id VARCHAR(50) UNIQUE,              -- SOP-001, SOP-002
  sop_name VARCHAR(255) NOT NULL,
  sop_version VARCHAR(20),
  
  purpose TEXT,
  description TEXT,
  applicable_roles TEXT[],                -- ['procurement', 'finance']
  
  -- Procedure content
  procedure_steps JSONB,                  -- Detailed steps with conditions
  approval_matrix JSONB,                  -- Who can do what
  threshold_rules JSONB,                  -- Amount/time limits
  required_documents TEXT[],              -- What to attach
  timeline_days INT,
  prerequisites TEXT[],                   -- What must be done first
  
  -- Vectorized for semantic search
  description_embedding VECTOR(1536),
  
  -- Source tracking
  source_doc_id INT REFERENCES sop_documents(id),
  page_numbers VARCHAR(50),               -- e.g., "1-5, 12"
  
  -- Metadata
  effective_date DATE,
  expiry_date DATE,
  owner_id INT REFERENCES users(id),
  last_reviewed_date DATE,
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_procedures_roles ON procedures USING GIN(applicable_roles);
CREATE INDEX idx_procedures_embedding ON procedures USING ivfflat(description_embedding);
CREATE INDEX idx_procedures_sop_id ON procedures(sop_id);

-- 3. Validation Rules
CREATE TABLE validation_rules (
  id SERIAL PRIMARY KEY,
  rule_id VARCHAR(50) UNIQUE,             -- RULE-001
  rule_name VARCHAR(255),
  
  -- Rule definition
  rule_type VARCHAR(50),                  -- approval, sequence, document, sla, threshold
  sop_reference VARCHAR(50),              -- SOP-003 Step 2
  
  -- Condition logic (stored as JSON for flexibility)
  condition_logic JSONB,                  -- {"field": "po_amount", "operator": ">=", "value": 100000000}
  check_function_name VARCHAR(255),       -- Name of validation function
  
  -- Messages
  violation_message TEXT,
  guidance_text TEXT,
  
  -- Severity & behavior
  severity VARCHAR(50),                   -- critical, high, medium, low
  blocking BOOLEAN DEFAULT false,         -- If true, prevent action
  auto_escalate BOOLEAN DEFAULT false,
  
  enabled BOOLEAN DEFAULT true,
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Compliance Events (Audit Trail)
CREATE TABLE compliance_events (
  id SERIAL PRIMARY KEY,
  event_id VARCHAR(50) UNIQUE,
  
  user_id INT REFERENCES users(id),
  action_type VARCHAR(100),               -- approve_po, create_tender, submit_quote
  entity_type VARCHAR(50),                -- purchase_order, tender, quote
  entity_id INT,
  
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  -- Compliance check result
  is_compliant BOOLEAN,
  sop_id VARCHAR(50) REFERENCES procedures(sop_id),
  
  violations JSONB,                       -- [{"rule": "approval_authority", "severity": "critical"}]
  
  user_action VARCHAR(50),                -- proceed, cancel, escalate
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_compliance_events_user ON compliance_events(user_id);
CREATE INDEX idx_compliance_events_entity ON compliance_events(entity_type, entity_id);
CREATE INDEX idx_compliance_events_sop ON compliance_events(sop_id);

-- 5. Compliance Violations Log
CREATE TABLE compliance_violations (
  id SERIAL PRIMARY KEY,
  violation_id VARCHAR(50) UNIQUE,
  
  event_id INT REFERENCES compliance_events(id),
  rule_id INT REFERENCES validation_rules(id),
  
  user_id INT REFERENCES users(id),
  action_type VARCHAR(100),
  
  violation_details JSONB,                -- Full context
  
  severity VARCHAR(50),                   -- critical, high, medium, low
  
  status VARCHAR(50),                     -- detected, acknowledged, resolved, reviewed
  acknowledged_at TIMESTAMP,
  acknowledged_by INT REFERENCES users(id),
  
  resolution_notes TEXT,
  resolved_at TIMESTAMP,
  resolved_by INT REFERENCES users(id),
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_violations_user ON compliance_violations(user_id);
CREATE INDEX idx_violations_status ON compliance_violations(status);
CREATE INDEX idx_violations_severity ON compliance_violations(severity);

-- 6. Chatbot Interactions
CREATE TABLE chatbot_interactions (
  id SERIAL PRIMARY KEY,
  interaction_id VARCHAR(50) UNIQUE,
  
  user_id INT REFERENCES users(id),
  user_query TEXT,
  
  intent VARCHAR(100),                    -- procedure_guidance, permission_check, sla_question
  intent_confidence DECIMAL(3,2),
  
  retrieved_sops TEXT[],                  -- SOP IDs retrieved
  
  chatbot_response TEXT,
  response_generated_at TIMESTAMP,
  
  user_satisfied BOOLEAN,                 -- Did user find answer helpful?
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_chatbot_user ON chatbot_interactions(user_id);

-- 7. Compliance Dashboard Metrics (Cached)
CREATE TABLE compliance_metrics (
  id SERIAL PRIMARY KEY,
  
  metric_date DATE,
  
  -- Overall compliance
  overall_compliance_score DECIMAL(5,2),  -- 0-100
  
  -- By category
  approval_authority_compliance DECIMAL(5,2),
  sla_compliance DECIMAL(5,2),
  documentation_compliance DECIMAL(5,2),
  sequence_compliance DECIMAL(5,2),
  threshold_compliance DECIMAL(5,2),
  
  -- Violation counts
  violations_critical INT DEFAULT 0,
  violations_high INT DEFAULT 0,
  violations_medium INT DEFAULT 0,
  violations_low INT DEFAULT 0,
  
  -- Per-user scores
  per_user_scores JSONB,                  -- {"user_id": score}
  
  -- Per-procedure adherence
  per_procedure_adherence JSONB,          -- {"SOP-001": 98.5, "SOP-002": 92.1}
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_metrics_date ON compliance_metrics(metric_date);

-- 8. SOP Update History (Version Control)
CREATE TABLE sop_version_history (
  id SERIAL PRIMARY KEY,
  sop_id VARCHAR(50),
  
  version VARCHAR(20),
  change_description TEXT,
  changed_by INT REFERENCES users(id),
  changed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  old_content JSONB,
  new_content JSONB,
  
  reason_for_change VARCHAR(50),          -- clarification, policy_update, error_fix
  
  FOREIGN KEY (sop_id) REFERENCES procedures(sop_id)
);

-- Add columns to existing procurement tables for compliance tracking

ALTER TABLE purchase_orders 
ADD COLUMN compliance_checked BOOLEAN DEFAULT false,
ADD COLUMN compliance_violations JSONB,
ADD COLUMN last_compliance_check TIMESTAMP;

ALTER TABLE tenders
ADD COLUMN sop_reference VARCHAR(50),     -- SOP-002
ADD COLUMN compliance_score DECIMAL(5,2);

ALTER TABLE payments
ADD COLUMN compliance_verified BOOLEAN DEFAULT false,
ADD COLUMN three_way_match_status VARCHAR(50);

```

---

## PART 2: BACKEND API IMPLEMENTATION

### 2.1 Procedure Validator Service

```python
# procedure_validator.py
# Real-time compliance checking service

from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
from enum import Enum
import json
import asyncio
from dataclasses import dataclass

import anthropic
from sqlalchemy import create_engine, select
from pinecone import Pinecone

# ===========================================
# DATA MODELS
# ===========================================

class Severity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

@dataclass
class ValidationResult:
    is_compliant: bool
    violations: List[Dict]
    sop_references: List[str]
    guidance: Optional[str]
    severity: Severity
    
class ProcedureValidator:
    """Main validator service"""
    
    def __init__(self, db_connection_string: str, pinecone_key: str):
        self.engine = create_engine(db_connection_string)
        self.pc = Pinecone(api_key=pinecone_key)
        self.client = anthropic.Anthropic()
        
    # ===========================================
    # MAIN VALIDATION ENTRY POINT
    # ===========================================
    
    async def validate_action(
        self,
        user_id: int,
        action_type: str,           # approve_po, create_tender, etc
        entity_type: str,           # purchase_order, tender, quote
        entity_id: int,
        context: Dict
    ) -> ValidationResult:
        """
        Main entry point: Validate a user action against procedures
        """
        
        print(f"🔍 VALIDATING: {action_type} on {entity_type}:{entity_id}")
        
        violations = []
        sop_refs = []
        
        # Step 1: Get relevant SOPs for this action
        relevant_sops = await self._find_relevant_sops(action_type, entity_type)
        
        if not relevant_sops:
            print(f"⚠️ No SOPs found for {action_type}")
            return ValidationResult(
                is_compliant=True,
                violations=[],
                sop_references=[],
                guidance="No SOPs defined for this action",
                severity=Severity.LOW
            )
        
        # Step 2: Get user info & role
        user_role = await self._get_user_role(user_id)
        
        # Step 3: Run each validation rule for relevant SOPs
        for sop in relevant_sops:
            rule_violations = await self._validate_against_sop(
                sop_id=sop['sop_id'],
                user_role=user_role,
                action_type=action_type,
                entity_type=entity_type,
                entity_id=entity_id,
                context=context
            )
            
            violations.extend(rule_violations)
            if rule_violations:
                sop_refs.append(sop['sop_id'])
        
        # Step 4: Determine overall compliance
        if not violations:
            is_compliant = True
            severity = Severity.LOW
            guidance = "✅ Action complies with all procedures"
        else:
            # Find highest severity violation
            severity_levels = {v['severity'] for v in violations}
            if Severity.CRITICAL.value in severity_levels:
                is_compliant = False
                severity = Severity.CRITICAL
            elif Severity.HIGH.value in severity_levels:
                is_compliant = False
                severity = Severity.HIGH
            else:
                is_compliant = True
                severity = Severity.MEDIUM
            
            guidance = await self._generate_guidance(violations, sop_refs)
        
        # Step 5: Log this validation event
        await self._log_compliance_event(
            user_id=user_id,
            action_type=action_type,
            entity_type=entity_type,
            entity_id=entity_id,
            is_compliant=is_compliant,
            violations=violations,
            sop_references=sop_refs
        )
        
        return ValidationResult(
            is_compliant=is_compliant,
            violations=violations,
            sop_references=sop_refs,
            guidance=guidance,
            severity=severity
        )
    
    # ===========================================
    # HELPER METHODS
    # ===========================================
    
    async def _find_relevant_sops(
        self,
        action_type: str,
        entity_type: str
    ) -> List[Dict]:
        """Find SOPs relevant to this action"""
        
        # Build semantic search query
        query = f"{entity_type} {action_type}"
        
        # Search vector DB
        query_embedding = self.client.embeddings.create(
            input=query,
            model="text-embedding-3-small"
        ).data[0].embedding
        
        # Query Pinecone for relevant procedures
        index = self.pc.Index("procedures")
        results = index.query(
            vector=query_embedding,
            top_k=5,
            include_metadata=True
        )
        
        sops = []
        with self.engine.connect() as conn:
            for match in results['matches']:
                sop_id = match['metadata']['sop_id']
                sop = conn.execute(
                    select(procedures).where(procedures.c.sop_id == sop_id)
                ).fetchone()
                if sop:
                    sops.append(dict(sop))
        
        return sops
    
    async def _get_user_role(self, user_id: int) -> str:
        """Get user's role from database"""
        with self.engine.connect() as conn:
            result = conn.execute(
                f"SELECT role FROM users WHERE id = {user_id}"
            ).fetchone()
            return result[0] if result else "user"
    
    async def _validate_against_sop(
        self,
        sop_id: str,
        user_role: str,
        action_type: str,
        entity_type: str,
        entity_id: int,
        context: Dict
    ) -> List[Dict]:
        """
        Validate action against specific SOP
        Returns list of violations found
        """
        
        violations = []
        
        with self.engine.connect() as conn:
            sop = conn.execute(
                f"SELECT * FROM procedures WHERE sop_id = '{sop_id}'"
            ).fetchone()
        
        if not sop:
            return violations
        
        sop_dict = dict(sop)
        
        # Rule 1: Check Approval Authority
        if 'approval_matrix' in sop_dict and sop_dict['approval_matrix']:
            auth_violation = await self._check_approval_authority(
                sop_id=sop_id,
                user_role=user_role,
                context=context
            )
            if auth_violation:
                violations.append(auth_violation)
        
        # Rule 2: Check Prerequisites
        if 'prerequisites' in sop_dict and sop_dict['prerequisites']:
            prereq_violation = await self._check_prerequisites(
                entity_id=entity_id,
                entity_type=entity_type,
                prerequisites=sop_dict['prerequisites']
            )
            if prereq_violation:
                violations.append(prereq_violation)
        
        # Rule 3: Check Required Documents
        if 'required_documents' in sop_dict and sop_dict['required_documents']:
            doc_violation = await self._check_required_documents(
                entity_id=entity_id,
                required_docs=sop_dict['required_documents']
            )
            if doc_violation:
                violations.append(doc_violation)
        
        # Rule 4: Check Timeline/SLA
        if 'timeline_days' in sop_dict and sop_dict['timeline_days']:
            sla_violation = await self._check_sla(
                entity_id=entity_id,
                entity_type=entity_type,
                timeline_days=sop_dict['timeline_days']
            )
            if sla_violation:
                violations.append(sla_violation)
        
        # Rule 5: Check Amount Thresholds
        if 'threshold_rules' in sop_dict and sop_dict['threshold_rules']:
            threshold_violation = await self._check_thresholds(
                sop_id=sop_id,
                context=context
            )
            if threshold_violation:
                violations.append(threshold_violation)
        
        return violations
    
    async def _check_approval_authority(
        self,
        sop_id: str,
        user_role: str,
        context: Dict
    ) -> Optional[Dict]:
        """Check if user has authority to perform this action"""
        
        with self.engine.connect() as conn:
            sop = conn.execute(
                f"SELECT approval_matrix FROM procedures WHERE sop_id = '{sop_id}'"
            ).fetchone()
        
        if not sop:
            return None
        
        approval_matrix = json.loads(sop[0]) if isinstance(sop[0], str) else sop[0]
        
        # Check if user's role is in approval list
        rules = approval_matrix.get('rules', [])
        
        po_amount = context.get('amount', 0)
        
        authorized = False
        for rule in rules:
            amount_range = rule.get('amount_range')
            approver_role = rule.get('approver')
            
            # Parse amount range (e.g., "100000001-500000000")
            if '-' in str(amount_range):
                min_amt, max_amt = map(int, str(amount_range).split('-'))
                if min_amt <= po_amount <= max_amt and approver_role == user_role:
                    authorized = True
                    break
        
        if not authorized:
            return {
                'rule_id': 'approval_authority',
                'rule_name': 'User must have approval authority',
                'severity': 'critical',
                'message': f'Role {user_role} is not authorized to approve PO of {po_amount}',
                'sop_reference': sop_id,
                'guidance': 'Route to appropriate approver'
            }
        
        return None
    
    async def _check_prerequisites(
        self,
        entity_id: int,
        entity_type: str,
        prerequisites: List[str]
    ) -> Optional[Dict]:
        """Check if prerequisites have been completed"""
        
        # Map prerequisites to database checks
        prerequisite_checks = {
            'tender_closed': lambda: self._is_tender_closed(entity_id),
            'finance_reviewed': lambda: self._is_finance_reviewed(entity_id),
            'grn_created': lambda: self._is_grn_created(entity_id),
            'quote_evaluated': lambda: self._is_quote_evaluated(entity_id)
        }
        
        for prereq in prerequisites:
            if prereq in prerequisite_checks:
                is_met = await prerequisite_checks[prereq]()
                if not is_met:
                    return {
                        'rule_id': 'prerequisite',
                        'rule_name': 'Prerequisite not met',
                        'severity': 'critical',
                        'message': f'Prerequisite "{prereq}" not completed',
                        'guidance': f'Complete {prereq} first'
                    }
        
        return None
    
    async def _check_required_documents(
        self,
        entity_id: int,
        required_docs: List[str]
    ) -> Optional[Dict]:
        """Check if all required documents are attached"""
        
        with self.engine.connect() as conn:
            # Get attached documents for this entity
            result = conn.execute(
                f"SELECT array_agg(document_type) FROM attachments WHERE entity_id = {entity_id}"
            ).fetchone()
        
        attached_docs = result[0] if result[0] else []
        
        missing_docs = [doc for doc in required_docs if doc not in attached_docs]
        
        if missing_docs:
            return {
                'rule_id': 'required_documents',
                'rule_name': 'Missing required documents',
                'severity': 'high',
                'message': f'Missing documents: {", ".join(missing_docs)}',
                'guidance': f'Attach: {", ".join(missing_docs)}'
            }
        
        return None
    
    async def _check_sla(
        self,
        entity_id: int,
        entity_type: str,
        timeline_days: int
    ) -> Optional[Dict]:
        """Check if SLA deadline is being met"""
        
        with self.engine.connect() as conn:
            # Get creation date
            table_map = {
                'purchase_order': 'purchase_orders',
                'tender': 'tenders'
            }
            table = table_map.get(entity_type)
            
            if table:
                result = conn.execute(
                    f"SELECT created_at FROM {table} WHERE id = {entity_id}"
                ).fetchone()
                
                if result:
                    created_date = result[0]
                    days_elapsed = (datetime.now() - created_date).days
                    
                    if days_elapsed > timeline_days:
                        return {
                            'rule_id': 'sla_breach',
                            'rule_name': 'SLA Timeline Breached',
                            'severity': 'high',
                            'message': f'SLA breached: {days_elapsed} days elapsed, limit is {timeline_days}',
                            'guidance': 'Expedite action immediately'
                        }
        
        return None
    
    async def _check_thresholds(
        self,
        sop_id: str,
        context: Dict
    ) -> Optional[Dict]:
        """Check amount thresholds and other limits"""
        
        po_amount = context.get('amount', 0)
        
        # Example: If amount > 10B, might need additional approval
        if po_amount > 10_000_000_000:
            return {
                'rule_id': 'high_amount_threshold',
                'rule_name': 'High amount requires additional review',
                'severity': 'medium',
                'message': f'Amount {po_amount} exceeds normal threshold',
                'guidance': 'Consider splitting into multiple POs or get Direktur Keuangan, SDM dan Umum approval'
            }
        
        return None
    
    # Helper checks
    async def _is_tender_closed(self, tender_id: int) -> bool:
        with self.engine.connect() as conn:
            result = conn.execute(
                f"SELECT status FROM tenders WHERE id = {tender_id}"
            ).fetchone()
            return result[0] in ['closed', 'awarded'] if result else False
    
    async def _is_finance_reviewed(self, po_id: int) -> bool:
        with self.engine.connect() as conn:
            result = conn.execute(
                f"SELECT finance_reviewed FROM purchase_orders WHERE id = {po_id}"
            ).fetchone()
            return result[0] if result else False
    
    async def _is_grn_created(self, po_id: int) -> bool:
        with self.engine.connect() as conn:
            result = conn.execute(
                f"SELECT COUNT(*) FROM grn_records WHERE po_id = {po_id}"
            ).fetchone()
            return result[0] > 0 if result else False
    
    async def _is_quote_evaluated(self, tender_id: int) -> bool:
        with self.engine.connect() as conn:
            result = conn.execute(
                f"SELECT status FROM tenders WHERE id = {tender_id}"
            ).fetchone()
            return result[0] in ['evaluated', 'closed', 'awarded'] if result else False
    
    async def _generate_guidance(
        self,
        violations: List[Dict],
        sop_refs: List[str]
    ) -> str:
        """Use Claude to generate helpful guidance"""
        
        violation_text = "\n".join([
            f"- {v['message']} (SOP: {v.get('sop_reference', 'N/A')})"
            for v in violations
        ])
        
        prompt = f"""
        A user has violations against company procedures:
        
        {violation_text}
        
        Generate a concise, helpful guidance message explaining:
        1. Why these violations matter
        2. What the correct procedure is
        3. Next steps to fix the issue
        
        Keep it friendly and professional (Indonesian style if needed).
        """
        
        response = self.client.messages.create(
            model="claude-opus-4-20250514",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text
    
    async def _log_compliance_event(
        self,
        user_id: int,
        action_type: str,
        entity_type: str,
        entity_id: int,
        is_compliant: bool,
        violations: List[Dict],
        sop_references: List[str]
    ):
        """Log this compliance check to audit trail"""
        
        with self.engine.connect() as conn:
            conn.execute(f"""
                INSERT INTO compliance_events 
                (user_id, action_type, entity_type, entity_id, is_compliant, violations)
                VALUES 
                ({user_id}, '{action_type}', '{entity_type}', {entity_id}, {is_compliant}, '{json.dumps(violations)}')
            """)
            conn.commit()
```

### 2.2 Chatbot Service

```python
# chatbot_service.py
# AI-powered guidance chatbot

import anthropic
from sqlalchemy import create_engine
from pinecone import Pinecone
import json

class ProcedureGuidanceBot:
    """Chatbot for answering SOP questions"""
    
    def __init__(self, db_connection: str, pinecone_key: str):
        self.client = anthropic.Anthropic()
        self.engine = create_engine(db_connection)
        self.pc = Pinecone(api_key=pinecone_key)
    
    async def answer_question(
        self,
        user_id: int,
        user_query: str,
        user_role: str
    ) -> Dict:
        """
        Main entry point for chatbot
        User asks question → Bot retrieves relevant SOPs → Bot answers
        """
        
        # Step 1: Classify intent
        intent = await self._classify_intent(user_query)
        
        # Step 2: Retrieve relevant procedures
        relevant_sops = await self._retrieve_relevant_sops(user_query, user_role)
        
        # Step 3: Generate response using Claude
        response = await self._generate_response(
            query=user_query,
            intent=intent,
            sops=relevant_sops,
            user_role=user_role
        )
        
        # Step 4: Log interaction
        await self._log_interaction(
            user_id=user_id,
            query=user_query,
            intent=intent,
            sops_used=[sop['sop_id'] for sop in relevant_sops],
            response=response
        )
        
        return {
            'intent': intent,
            'response': response,
            'sops_referenced': [sop['sop_id'] for sop in relevant_sops],
            'user_satisfaction_question': 'Was this helpful? [YES] [NO]'
        }
    
    async def _classify_intent(self, query: str) -> str:
        """Classify what user is asking about"""
        
        prompt = f"""
        Classify the user's question into ONE of these categories:
        - PROCEDURE_GUIDANCE: Asking how to do something (step-by-step)
        - PERMISSION_CHECK: Asking if they can do something
        - SLA_QUESTION: Asking about timeline or deadline
        - THRESHOLD_QUESTION: Asking about limits (amount, count)
        - ERROR_RECOVERY: Asking how to fix something wrong
        - GENERAL_INFO: General information about procedures
        
        User query: "{query}"
        
        Respond with ONLY the category name.
        """
        
        response = self.client.messages.create(
            model="claude-opus-4-20250514",
            max_tokens=50,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text.strip()
    
    async def _retrieve_relevant_sops(
        self,
        query: str,
        user_role: str
    ) -> List[Dict]:
        """Use semantic search to find relevant SOPs"""
        
        # Get embedding for query
        embedding = self.client.embeddings.create(
            input=query,
            model="text-embedding-3-small"
        ).data[0].embedding
        
        # Query Pinecone
        index = self.pc.Index("procedures")
        results = index.query(
            vector=embedding,
            top_k=3,
            include_metadata=True,
            filter={
                "applicable_roles": {"$in": [user_role]}
            }
        )
        
        # Fetch full SOP details from DB
        sops = []
        with self.engine.connect() as conn:
            for match in results['matches']:
                sop_id = match['metadata']['sop_id']
                result = conn.execute(
                    f"SELECT * FROM procedures WHERE sop_id = '{sop_id}'"
                ).fetchone()
                if result:
                    sops.append(dict(result))
        
        return sops
    
    async def _generate_response(
        self,
        query: str,
        intent: str,
        sops: List[Dict],
        user_role: str
    ) -> str:
        """Use Claude to generate helpful response"""
        
        # Build context from SOPs
        sop_context = "\n\n".join([
            f"SOP-{sop['sop_id']}:\n{sop['sop_name']}\n" +
            f"Steps: {json.dumps(sop['procedure_steps'], indent=2)}"
            for sop in sops
        ])
        
        prompt = f"""
        You are a helpful SOP assistant for a procurement system.
        User role: {user_role}
        User query: "{query}"
        Intent: {intent}
        
        RELEVANT PROCEDURES:
        {sop_context}
        
        Based on the procedures above, provide a helpful, clear answer to the user's question.
        
        Format your response:
        1. Answer the question directly
        2. Reference specific SOP steps
        3. Provide actionable next steps
        4. Use friendly, professional tone (Indonesian context preferred)
        
        If the user is asking permission to do something, clearly state if they can/cannot and why.
        """
        
        response = self.client.messages.create(
            model="claude-opus-4-20250514",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text
    
    async def _log_interaction(
        self,
        user_id: int,
        query: str,
        intent: str,
        sops_used: List[str],
        response: str
    ):
        """Log chatbot interaction to database"""
        
        with self.engine.connect() as conn:
            conn.execute(f"""
                INSERT INTO chatbot_interactions
                (user_id, user_query, intent, retrieved_sops, chatbot_response)
                VALUES
                ({user_id}, '{query.replace("'", "''")}', '{intent}', 
                 ARRAY{sops_used}, '{response.replace("'", "''")}')
            """)
            conn.commit()
```

---

## PART 3: FRONTEND IMPLEMENTATION

### 3.1 Validation Alert Component (React)

```jsx
// ValidationAlert.jsx
// Displays when user action violates procedure

import React, { useState } from 'react';
import './ValidationAlert.css';

export const ValidationAlert = ({ violation, onProceed, onCancel }) => {
  const [expanded, setExpanded] = useState(false);
  
  const getSeverityColor = (severity) => {
    switch (severity) {
      case 'critical': return '#ff0000';
      case 'high': return '#ff6600';
      case 'medium': return '#ffaa00';
      default: return '#0088ff';
    }
  };
  
  const getSeverityEmoji = (severity) => {
    switch (severity) {
      case 'critical': return '🔴';
      case 'high': return '🟠';
      case 'medium': return '🟡';
      default: return '🟢';
    }
  };
  
  return (
    <div className="validation-alert" style={{ borderLeftColor: getSeverityColor(violation.severity) }}>
      <div className="alert-header">
        <span className="severity-emoji">{getSeverityEmoji(violation.severity)}</span>
        <h3>ACTION NOT ALLOWED</h3>
        <button className="close-btn" onClick={onCancel}>×</button>
      </div>
      
      <div className="alert-content">
        <p className="alert-title">{violation.violations[0]?.message || 'Procedure violation detected'}</p>
        
        <div className="violations-list">
          <h4>Reasons:</h4>
          {violation.violations.map((v, idx) => (
            <div key={idx} className="violation-item">
              <span className="violation-icon">⚠️</span>
              <div className="violation-text">
                <strong>{v.rule_name}:</strong> {v.message}
                <br/>
                <small>SOP Reference: {v.sop_reference}</small>
              </div>
            </div>
          ))}
        </div>
        
        <div className="guidance-section">
          <h4>📋 CORRECT PROCEDURE:</h4>
          <p>{violation.guidance}</p>
        </div>
        
        <button 
          className="expand-btn"
          onClick={() => setExpanded(!expanded)}
        >
          {expanded ? '▼ Hide Details' : '▶ View Full SOP'}
        </button>
        
        {expanded && (
          <div className="sop-details">
            {violation.sop_references.map(sopId => (
              <div key={sopId} className="sop-content">
                <strong>SOP: {sopId}</strong>
                <p>[Full SOP content would display here]</p>
              </div>
            ))}
          </div>
        )}
      </div>
      
      <div className="alert-actions">
        <button className="btn-cancel" onClick={onCancel}>
          CANCEL ACTION
        </button>
        {!violation.violations.some(v => v.severity === 'critical') && (
          <button className="btn-proceed" onClick={onProceed}>
            ACKNOWLEDGE & PROCEED
          </button>
        )}
        <button className="btn-help">
          💬 ASK CHATBOT
        </button>
      </div>
    </div>
  );
};
```

### 3.2 Chatbot Widget (React)

```jsx
// ChatbotWidget.jsx
// AI-powered guidance chatbot in sidebar

import React, { useState, useRef, useEffect } from 'react';
import './ChatbotWidget.css';

export const ChatbotWidget = ({ userId, userRole }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { type: 'bot', text: 'Hi! I can help you understand procedures. What do you need help with?' }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);
  
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };
  
  useEffect(() => {
    scrollToBottom();
  }, [messages]);
  
  const handleSendMessage = async (e) => {
    e.preventDefault();
    
    if (!input.trim()) return;
    
    // Add user message
    setMessages(prev => [...prev, { type: 'user', text: input }]);
    setInput('');
    setLoading(true);
    
    try {
      // Call chatbot API
      const response = await fetch('/api/chatbot/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_id: userId,
          query: input,
          user_role: userRole
        })
      });
      
      const data = await response.json();
      
      // Add bot response
      setMessages(prev => [...prev, { 
        type: 'bot', 
        text: data.response,
        sops_referenced: data.sops_referenced,
        intent: data.intent
      }]);
    } catch (error) {
      setMessages(prev => [...prev, { 
        type: 'bot', 
        text: '❌ Error connecting to chatbot. Try again.' 
      }]);
    } finally {
      setLoading(false);
    }
  };
  
  return (
    <div className={`chatbot-widget ${isOpen ? 'open' : 'closed'}`}>
      {isOpen ? (
        <div className="chatbot-container">
          <div className="chatbot-header">
            <h3>📚 Procedure Guide</h3>
            <button onClick={() => setIsOpen(false)}>−</button>
          </div>
          
          <div className="chatbot-messages">
            {messages.map((msg, idx) => (
              <div key={idx} className={`message message-${msg.type}`}>
                {msg.type === 'bot' && <span className="bot-icon">🤖</span>}
                <div className="message-content">
                  {msg.text}
                  {msg.sops_referenced && (
                    <div className="sop-references">
                      <small>📖 Referenced: {msg.sops_referenced.join(', ')}</small>
                    </div>
                  )}
                </div>
              </div>
            ))}
            {loading && (
              <div className="message message-bot">
                <span className="bot-icon">🤖</span>
                <div className="message-content">Thinking...</div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
          
          <form onSubmit={handleSendMessage} className="chatbot-input">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask about procedures..."
              disabled={loading}
            />
            <button type="submit" disabled={loading}>Send</button>
          </form>
        </div>
      ) : (
        <button 
          className="chatbot-toggle"
          onClick={() => setIsOpen(true)}
          title="Ask for procedure guidance"
        >
          💬
        </button>
      )}
    </div>
  );
};
```

### 3.3 API Validation Interceptor

```javascript
// api-validator-interceptor.js
// Intercepts API calls and validates before executing

import axios from 'axios';

const createValidatedAPIClient = (userId, userRole) => {
  const client = axios.create();
  
  // Request interceptor: Validate before sending
  client.interceptors.request.use(
    async (config) => {
      // Extract action details from request
      const action = extractActionDetails(config);
      
      if (action) {
        // Call validation service
        const validation = await fetch('/api/validate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            user_id: userId,
            action_type: action.type,
            entity_type: action.entity,
            entity_id: action.id,
            context: action.context
          })
        }).then(r => r.json());
        
        // Handle validation result
        if (!validation.is_compliant && validation.severity === 'critical') {
          // Block the action
          showValidationAlert(validation);
          return Promise.reject({
            config,
            message: 'Action blocked due to procedure violation',
            validation
          });
        } else if (!validation.is_compliant) {
          // Show warning but allow proceeding
          showWarning(validation);
        }
        
        // Attach validation metadata
        config.headers['X-Validation-ID'] = validation.event_id;
      }
      
      return config;
    },
    error => Promise.reject(error)
  );
  
  return client;
};

const extractActionDetails = (config) => {
  // Parse URL and method to determine action
  const url = config.url;
  const method = config.method.toUpperCase();
  
  if (url.includes('/purchase-orders') && method === 'POST') {
    return {
      type: 'create_po',
      entity: 'purchase_order',
      id: null,
      context: config.data
    };
  }
  
  if (url.includes('/purchase-orders') && method === 'PATCH' && url.includes('/approve')) {
    const id = extractIdFromUrl(url);
    return {
      type: 'approve_po',
      entity: 'purchase_order',
      id: id,
      context: config.data
    };
  }
  
  // Add more action mappings...
  
  return null;
};

const extractIdFromUrl = (url) => {
  const match = url.match(/\/(\d+)/);
  return match ? parseInt(match[1]) : null;
};

export default createValidatedAPIClient;
```

---

## PART 4: DATABASE INITIALIZATION SCRIPT

```sql
-- initialize-guardian-system.sql

-- Insert sample validation rules

INSERT INTO validation_rules (rule_id, rule_name, rule_type, sop_reference, condition_logic, severity, blocking)
VALUES 
('RULE-001', 'PO Amount Threshold Check', 'threshold', 'SOP-003', '{"field":"po_amount","operator":">=","value":500000000}', 'high', true),
('RULE-002', 'Approval Authority Verification', 'approval', 'SOP-003', '{"check":"user_role_in_approvers"}', 'critical', true),
('RULE-003', 'SLA Timeline Compliance', 'sla', 'SOP-003', '{"max_days":2}', 'high', false),
('RULE-004', '3-Way Match Requirement', 'document', 'SOP-004', '{"required":["po","grn","invoice"]}', 'high', true);

-- Grant permissions for guardian service

GRANT ALL PRIVILEGES ON procedures TO guardian_service;
GRANT ALL PRIVILEGES ON validation_rules TO guardian_service;
GRANT ALL PRIVILEGES ON compliance_events TO guardian_service;
GRANT ALL PRIVILEGES ON compliance_violations TO guardian_service;
GRANT ALL PRIVILEGES ON chatbot_interactions TO guardian_service;

-- Create indexes for performance

CREATE INDEX idx_compliance_fast ON compliance_events(user_id, entity_type, created_at);
CREATE INDEX idx_violations_severity_date ON compliance_violations(severity, created_at);
CREATE INDEX idx_sop_procedures ON procedures(sop_id, effective_date);
```

---

## PART 5: DEPLOYMENT CHECKLIST

```
AI PROCEDURE GUARDIAN - DEPLOYMENT CHECKLIST

[ ] PHASE 1: SETUP (Week 1)
    [ ] Set up PostgreSQL database
    [ ] Run database initialization scripts
    [ ] Create vector DB (Pinecone account & index)
    [ ] Set up API keys (Anthropic, Pinecone)
    [ ] Test database connections
    
[ ] PHASE 2: BACKEND DEPLOYMENT (Week 1-2)
    [ ] Deploy validator service (Python)
    [ ] Deploy chatbot service (Python)
    [ ] Deploy API endpoints (Node.js)
    [ ] Test validation rules engine
    [ ] Test chatbot with sample queries
    [ ] Load test: 100 concurrent validations/sec
    
[ ] PHASE 3: DOCUMENT INGESTION (Week 2)
    [ ] Collect all SOP documents from KMU
    [ ] Prepare documents (scan if needed)
    [ ] Upload documents to system
    [ ] Run Gemini extraction on each doc
    [ ] Validate extraction quality
    [ ] Index procedures in vector DB
    [ ] Test semantic search
    
[ ] PHASE 4: FRONTEND DEPLOYMENT (Week 2-3)
    [ ] Deploy React components
    [ ] Integrate validation alerts
    [ ] Integrate chatbot widget
    [ ] Integrate API interceptor
    [ ] Test UI/UX flow
    [ ] Mobile responsiveness testing
    
[ ] PHASE 5: INTEGRATION (Week 3)
    [ ] Integrate validator with procurement API
    [ ] Integrate chatbot with messaging system
    [ ] Connect to email notifications
    [ ] Test end-to-end workflows
    [ ] Performance testing
    
[ ] PHASE 6: TESTING & UAT (Week 3-4)
    [ ] Unit tests (80%+ coverage)
    [ ] Integration tests
    [ ] User acceptance testing with KMU team
    [ ] Security audit
    [ ] Compliance testing
    [ ] Documentation review
    
[ ] PHASE 7: TRAINING & GO-LIVE (Week 4)
    [ ] User training sessions
    [ ] Administrator training
    [ ] Documentation handoff
    [ ] Go-live date set
    [ ] Support team briefing
    [ ] Monitor for issues first week

SUCCESS METRICS:
✅ Procedure compliance rate: 95%+
✅ System uptime: 99.9%+
✅ Validation latency: <500ms
✅ User adoption: 80%+ within 2 weeks
✅ Support tickets: <5 per week
```

---

## PART 6: EXAMPLE API CALLS

### Validate a PO Approval

```bash
curl -X POST http://localhost:3000/api/validate \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 42,
    "action_type": "approve_po",
    "entity_type": "purchase_order",
    "entity_id": 100,
    "context": {
      "po_amount": 350000000,
      "budget_code": "EQP-2025-Q2"
    }
  }'

Response:
{
  "is_compliant": false,
  "violations": [
    {
      "rule_id": "approval_authority",
      "message": "Kepala Bagian Keuangan can approve 100M-500M, but PO needs Finance review first",
      "severity": "high",
      "sop_reference": "SOP-003, Step 2"
    }
  ],
  "sop_references": ["SOP-003"],
  "guidance": "This PO needs Kepala Bagian Keuangan review before approval...",
  "severity": "high"
}
```

### Ask Chatbot

```bash
curl -X POST http://localhost:3000/api/chatbot/ask \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 42,
    "user_role": "finance_manager",
    "query": "How do I approve a PO?"
  }'

Response:
{
  "intent": "PROCEDURE_GUIDANCE",
  "response": "Based on your role (Kepala Bagian Keuangan), here's how to approve a PO...[full step-by-step guidance]",
  "sops_referenced": ["SOP-003"],
  "user_satisfaction_question": "Was this helpful? [YES] [NO]"
}
```

---

## READY TO IMPLEMENT! 🚀

IT Team dapat langsung:
1. Run SQL scripts untuk create database
2. Deploy Python services (validator + chatbot)
3. Deploy Node.js API endpoints
4. Deploy React components
5. Upload SOP documents
6. Run testing & UAT
7. Go live!

**No ambiguity. Everything specified.**

