def get_send_arguments(mock_send):
    sender, recipients, template, context, batch_id, object_ids, version = mock_send.call_args_list[0][0][0]
    return {
        "sender": sender,
        "recipients": recipients,
        "template": template,
        "context": context,
        "batch_id": batch_id,
        "object_ids": object_ids,
        "version": version
    }