class InlineOptions:

    @staticmethod
    def automatic():
        from approvaltests.namer.inline_python_reporter import InlinePythonReporter
        from approvaltests.reporters import ReporterThatAutomaticallyApproves

        class AutomaticInlineOptions(InlineOptions):
            def apply(self, options: "Options") -> "Options":
                return options.with_reporter(
                    InlinePythonReporter(ReporterThatAutomaticallyApproves())
                )

        return AutomaticInlineOptions()

    @staticmethod
    def semi_automatic():
        from approvaltests.namer.inline_python_reporter import InlinePythonReporter
        from approvaltests.reporters import ReporterThatAutomaticallyApproves

        class SemiAutomaticInlineOptions(InlineOptions):
            def apply(self, options: "Options") -> "Options":
                return options.with_reporter(
                    InlinePythonReporter(
                        ReporterThatAutomaticallyApproves(), add_approval_line=True
                    )
                )

        return SemiAutomaticInlineOptions()

    @staticmethod
    def applesauce():
        return InlineOptions()

    def apply(self, options: "Options") -> "Options":

        return options

    @staticmethod
    def show_code(do_show_code: bool = True):
        from approvaltests.namer.inline_python_reporter import InlinePythonReporter

        class ShowCodeInlineOptions(InlineOptions):
            def apply(self, options: "Options") -> "Options":
                return options.with_reporter(InlinePythonReporter(options.reporter))

        class DoNotShowCodeInlineOptions(InlineOptions):
            def apply(self, options: "Options") -> "Options":
                return options

        return ShowCodeInlineOptions() if do_show_code else DoNotShowCodeInlineOptions()
