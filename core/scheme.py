from ninja import Schema

class TopicSchema(Schema):
    id: int
    title: str
    content: str
    course_id: int
