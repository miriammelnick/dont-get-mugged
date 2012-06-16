
###############################################################################
#
# ListMergeVarAdd
# Add a new field to a MailChimp list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListMergeVarAdd(Choreography):

    """
    Create a new instance of the ListMergeVarAdd Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListMergeVarAdd')


    def new_input_set(self):
        return ListMergeVarAddInputSet()

    def _make_result_set(self, result, path):
        return ListMergeVarAddResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListMergeVarAddChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListMergeVarAdd
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListMergeVarAddInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Mailchimp.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Choices input for this choreography. ((optional, string) A list of up to 10 choices for radio and dropdown type fields )separated by commas).)
        """
        def set_Choices(self, value):
            InputSet._set_input(self, 'Choices', value)

        """
        Set the value of the DateFormat input for this choreography. ((optional, string) Valid for birthday and date fields. For birthday, must be "MM/DD" (default) or "DD/MM". For date type, must be "MM/DD/YYYY" (default) or "DD/MM/YYYY".)
        """
        def set_DateFormat(self, value):
            InputSet._set_input(self, 'DateFormat', value)

        """
        Set the value of the DefaultCountry input for this choreography. ((optional, string) The ISO 3166 2 digit character code for the default country. Defaults to "US".)
        """
        def set_DefaultCountry(self, value):
            InputSet._set_input(self, 'DefaultCountry', value)

        """
        Set the value of the DefaultValue input for this choreography. ((optional, string) The default value for the new field.)
        """
        def set_DefaultValue(self, value):
            InputSet._set_input(self, 'DefaultValue', value)

        """
        Set the value of the FieldType input for this choreography. ((optional, string) Must be either left unset or one of 'text', 'number', 'radio', 'dropdown', 'date', 'address', 'phone', 'url', or 'imageurl. Defaults to text.)
        """
        def set_FieldType(self, value):
            InputSet._set_input(self, 'FieldType', value)

        """
        Set the value of the ListId input for this choreography. ((required, string) The ID of the list on which to add the new merge var.)
        """
        def set_ListId(self, value):
            InputSet._set_input(self, 'ListId', value)

        """
        Set the value of the Name input for this choreography. ((required, string) Provide a long merge var name for user display (i.e. First Name))
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the PhoneFormat input for this choreography. ((optional, string) Defaults to "US"  - any other value will cause them to be unformatted (international).)
        """
        def set_PhoneFormat(self, value):
            InputSet._set_input(self, 'PhoneFormat', value)

        """
        Set the value of the Public input for this choreography. ((optional, boolean) Indicates whether the field is displayed in public. Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        def set_Public(self, value):
            InputSet._set_input(self, 'Public', value)

        """
        Set the value of the Req input for this choreography. ((optional, boolean) Indicates that the field will be required.  Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        def set_Req(self, value):
            InputSet._set_input(self, 'Req', value)

        """
        Set the value of the Show input for this choreography. ((optional, boolean) Indicates whether the field is displayed in the app's list member view.  Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        def set_Show(self, value):
            InputSet._set_input(self, 'Show', value)

        """
        Set the value of the Tag input for this choreography. ((required, string) Provide a short merge var tag name. MUST be 10 UTF-8 chars, including 'A-Z', '0-9', or '_' only (i.e. DESC123456).)
        """
        def set_Tag(self, value):
            InputSet._set_input(self, 'Tag', value)


"""
A ResultSet with methods tailored to the values returned by the ListMergeVarAdd choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListMergeVarAddResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) The response from Mailchimp. Returns the string "true" for success and "false" for failures.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListMergeVarAddChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListMergeVarAddResultSet(response, path)
