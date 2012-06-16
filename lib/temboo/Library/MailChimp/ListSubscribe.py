
###############################################################################
#
# ListSubscribe
# Adds a subscriber to a MailChimp list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListSubscribe(Choreography):

    """
    Create a new instance of the ListSubscribe Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListSubscribe')


    def new_input_set(self):
        return ListSubscribeInputSet()

    def _make_result_set(self, result, path):
        return ListSubscribeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListSubscribeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListSubscribe
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListSubscribeInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Mailchimp.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the DoubleOptIn input for this choreography. ((optional, boolean) Flag to control whether a double opt-in confirmation message is sent. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        def set_DoubleOptIn(self, value):
            InputSet._set_input(self, 'DoubleOptIn', value)

        """
        Set the value of the EmailAddress input for this choreography. ((conditional, string) The email address for the subscriber you want to create. Required unless the email address is included in the MergeVars input as part of your JSON object.)
        """
        def set_EmailAddress(self, value):
            InputSet._set_input(self, 'EmailAddress', value)

        """
        Set the value of the EmailType input for this choreography. ((optional, string) Must be one of 'text', 'html', or 'mobile'. Defaults to html.)
        """
        def set_EmailType(self, value):
            InputSet._set_input(self, 'EmailType', value)

        """
        Set the value of the ListId input for this choreography. ((required, string) The id of the list that the subsbriber will be added to.)
        """
        def set_ListId(self, value):
            InputSet._set_input(self, 'ListId', value)

        """
        Set the value of the MergeVars input for this choreography. ((conditional, json) A JSON object of the merge fields for this subscriber. If the subscriber email address is not provided for the EmailAddress input, it must be specified here.)
        """
        def set_MergeVars(self, value):
            InputSet._set_input(self, 'MergeVars', value)

        """
        Set the value of the ReplaceInterests input for this choreography. ((optional, boolean) A flag to determine whether to replace the interest groups with the groups provided or add the provided groups to the member's interest groups. Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        def set_ReplaceInterests(self, value):
            InputSet._set_input(self, 'ReplaceInterests', value)

        """
        Set the value of the SendWelcome input for this choreography. ((optional, boolean) If double_optin is false and this flag is true, a welcome email will be sent. Note that this does not apply when updating records. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        def set_SendWelcome(self, value):
            InputSet._set_input(self, 'SendWelcome', value)

        """
        Set the value of the UpdateExisting input for this choreography. ((optional, boolean) Indicates that if the email already exists, this request will perform an update instead of an insert. Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        def set_UpdateExisting(self, value):
            InputSet._set_input(self, 'UpdateExisting', value)


"""
A ResultSet with methods tailored to the values returned by the ListSubscribe choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListSubscribeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Mailchimp. Returns the string "true" for success and an error description for failures.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListSubscribeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListSubscribeResultSet(response, path)
