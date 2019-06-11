Serverless StackOverflow
==============================================================================


Virginia Cyber Range Challenge
------------------------------------------------------------------------------

Creation of the serverless forum or Q&A system. Like Stackoverflow with Serverless Architect



Our Work (Enquizit. Inc)
------------------------------------------------------------------------------

1. Create a Pure AWS Lambda powered Webapp.
2. There's no long-running server, only pay as you go.
3. Use S3 for front-end template
4. DocumentDB (AWS version of MongoDB) for Storage.
5. API Gateway with Cache to auto-scale with the traffic load.
6. Use Single Layer to Power many Lambda function, we can deploy the updates in 1 minutes, because we only update the function codes


Demo
------------------------------------------------------------------------------

1. Post List page
2. Create Post
3. Put Comment


The Design
------------------------------------------------------------------------------


Why MongoDB? Why Not DynamoDB Relational DB?
------------------------------------------------------------------------------

1. query based on many-to-many relationship requires lots of join
2. schema free, we have the flexibility to customize our query pattern, DocumentDB with built in standard SQL-liked search, tag search, full-text-search
3. greately simplify the query pattern, trade redundancy for simplicity.


Why API Gateway
------------------------------------------------------------------------------

1. Programmer API, standard CRUD for Database entity.
2. View Render API, get html from S3, get data from programmer API, and render the view.
3. It greatly isolated the frontend work and backend work.


.. code-block:: python

    # -*- coding: utf-8 -*-

    import attr
    from attrs_mate import AttrsClass


    @attr.s
    class Event(AttrsClass):
        author_id = attr.ib()
        post_id = attr.ib()
        content = attr.ib()


    def handler(event, context):
        from ..model.model import Post
        from ..api import LbdResponse

        try:
            event = Event(**event)
            comment = Post.post_comment(
                author_id=event.author_id,
                post_id=event.post_id,
                content=event.content
            )
            response = LbdResponse(
                data=comment_data,
                errors=list(),
                success=True,
                status=LbdResponse.StatusCode.Success
            )
        except Exception as e:
            response = LbdResponse(
                data=list(),
                errors=[(e.__class__.__name__, str(e))],
                success=False,
                status=LbdResponse.StatusCode.ServerError,
            )

        return response.to_dict()


.. code-block:: python

    class Post(BaseModel):
        title = me.fields.StringField(required=True)
        content = me.fields.StringField()
        create_at = me.fields.DateTimeField(default=lambda: datetime.utcnow())
        last_edited_at = me.fields.DateTimeField(default=lambda: datetime.utcnow())

        author = me.fields.EmbeddedDocumentField(Author)
        comments = me.fields.ListField(me.fields.EmbeddedDocumentField(Comment))


Use Layer and CI-CD
------------------------------------------------------------------------------

1. single deployment package for all functions.
2. put complex logic in ORM layer instead of lambda handler, so we can easily test before we deploy.
